from datetime import date, timedelta
from html import escape
import json
import os
from pathlib import Path
import re
import sys
from urllib.error import URLError
from urllib.request import Request, urlopen


PALETTE = ("#28394a", "#75d9bd", "#70c8f2", "#b79af2", "#ffc286")
LEGEND = ("0", "1", "2–3", "4–6", "7+")
MONO = "ui-monospace,Consolas,'Liberation Mono',monospace"
SANS = "'Trebuchet MS','Segoe UI',Verdana,sans-serif"


def api(url, token, body=None):
    headers = {"Authorization": "Bearer " + token, "Accept": "application/vnd.github+json",
               "User-Agent": "github-profile-activity", "X-GitHub-Api-Version": "2022-11-28"}
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode()
    with urlopen(Request(url, data=data, headers=headers), timeout=30) as response:
        return json.load(response)


def read_activity(owner, token):
    query = """query($login:String!){user(login:$login){contributionsCollection{
      contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}
    }}}"""
    result = api("https://api.github.com/graphql", token, {"query": query, "variables": {"login": owner}})
    if result.get("errors") or not result.get("data", {}).get("user"):
        raise ValueError("GitHub returned an incomplete contribution calendar")
    calendar = result["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    days = [day for week in calendar["weeks"] for day in week["contributionDays"]]
    try:
        events = api(f"https://api.github.com/users/{owner}/events/public?per_page=100", token)
    except (URLError, TimeoutError):
        events = []
    return {"total": calendar["totalContributions"], "days": days, "events": events}


def verified_days(snapshot):
    rows = sorted((date.fromisoformat(v["date"]), v["contributionCount"]) for v in snapshot["days"])
    total = snapshot["total"]
    if not isinstance(total, int) or total < 0 or len(rows) < 350 or len(rows) > 372:
        raise ValueError("Invalid annual contribution calendar")
    if any(type(n) is not int or n < 0 for _, n in rows):
        raise ValueError("Invalid daily contribution count")
    if any(b[0] - a[0] != timedelta(days=1) for a, b in zip(rows, rows[1:])):
        raise ValueError("Calendar has duplicate or missing dates")
    return rows


def recent_activity(owner, events, days):
    verbs = {"PushEvent": "Pushed code", "PullRequestEvent": "Pull request activity",
             "IssuesEvent": "Issue activity", "ReleaseEvent": "Published a release",
             "PullRequestReviewEvent": "Reviewed a pull request", "ForkEvent": "Forked a repository"}
    selected = []
    seen = set()
    for e in sorted(events, key=lambda item: item.get("created_at", ""), reverse=True):
        repo = e.get("repo", {}).get("name", "")
        if not e.get("public") or e.get("actor", {}).get("login", "").lower() != owner.lower():
            continue
        if not re.fullmatch(r"[\w.-]+/[\w.-]+", repo, re.ASCII):
            continue
        verb = verbs.get(e.get("type"))
        if e.get("type") == "CreateEvent":
            verb = {"repository": "Created a repository", "branch": "Created a branch",
                    "tag": "Created a tag"}.get((e.get("payload") or {}).get("ref_type"))
        if not verb:
            continue
        stamp = date.fromisoformat(e["created_at"][:10])
        if (stamp, repo, verb) in seen:
            continue
        seen.add((stamp, repo, verb))
        selected.append((stamp, verb, repo))
        if len(selected) == 3:
            break
    if selected:
        return "Recent public activity", selected
    return "Recent active days", [(day, f"{n} contribution" + ("s" if n != 1 else ""), "")
                                  for day, n in reversed(days) if n][:3]


def label(value, x, y, size, ink, weight=500, *, mono=False, anchor="start", spacing=0):
    return (f'<text x="{x}" y="{y}" fill="{ink}" font-size="{size}" font-weight="{weight}" '
            f'font-family="{MONO if mono else SANS}" text-anchor="{anchor}" letter-spacing="{spacing}">'
            f'{escape(str(value))}</text>')


def line(d, ink, width=1, extra=""):
    return f'<path d="{d}" fill="none" stroke="{ink}" stroke-width="{width}" stroke-linecap="round" {extra}/>'


def cell_level(n):
    return 0 if n == 0 else 1 if n == 1 else 2 if n <= 3 else 3 if n <= 6 else 4


def cell(x, y, n, size):
    level = cell_level(n)
    color = PALETTE[level]
    if not level:
        return f'<rect x="{x:.1f}" y="{y:.1f}" width="{size}" height="{size}" rx="2" fill="{color}"/>'
    height = 1.3 + level * .8
    shift = height * .55
    return (f'<path d="M{x:.1f} {y+1:.1f}h{size}v{size-1}l{-shift:.1f} {height:.1f}h{-size}v{-size}z" fill="{color}" opacity=".53"/>'
            f'<rect x="{x:.1f}" y="{y-height:.1f}" width="{size}" height="{size}" rx="2" fill="{color}"/>'
            + line(f"M{x+1.8:.1f} {y-height+1.1:.1f}h{size-3.6:.1f}", "#fcfff7", .8,'opacity=".65"'))


def calendar_strip(weeks, x, y, width, mobile):
    pitch = min(15.1 if mobile else 13.95, (width - 10) / max(1, len(weeks)))
    size = 9 if mobile else 9.1
    result = []
    last_month = None
    last_label = -50
    for index, week in enumerate(weeks):
        first = week[0][0]
        month = first.month
        if month != last_month and index - last_label >= 3:
            result.append(label(first.strftime("%b"), round(x + index*pitch), y-12, 12, "#c1ccdc", mono=True))
            last_label = index
            last_month = month
        for day, n in week:
            weekday = (day.weekday() + 1) % 7
            result.append(cell(x + index*pitch, y + weekday*12.4, n, size))
    for row, name in [(1, "M"), (3, "W"), (5, "F")]:
        result.append(label(name,x-10,round(y+row*12.4+8),11,"#a7b7c9",mono=True,anchor="end"))
    end = x + (len(weeks)-1)*pitch + size
    result.append(line(f"M{x} {y+90}H{end:.1f}", "#405469", 1))
    result.append(line(f"M{x} {y+90}H{end:.1f}", "#79d8c2", 1.6,
                       'class="scan" pathLength="100" stroke-dasharray="4 100" stroke-dashoffset="-25"'))
    return "".join(result)


def date_label(day):
    return f"{day.day} {day:%b %Y}"


def render(owner, snapshot, mobile=False):
    days = verified_days(snapshot)
    title, timeline = recent_activity(owner, snapshot.get("events", []), days)
    small = mobile
    w, h = (438, 594) if small else (882, 342)
    x = 21 if small else 27
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">',
           '<title>GitHub contributions and activity</title>',
           f'<desc>{snapshot["total"]} contributions in GitHub’s annual calendar through {date_label(days[-1][0])}. ',
           escape(title + ". " + " ".join(f"{date_label(d)}: {v} {r}." for d,v,r in timeline))+'</desc>',
           '<defs><linearGradient id="bg" x2=".85" y2="1"><stop stop-color="#192b37"/><stop offset=".55" stop-color="#172338"/><stop offset="1" stop-color="#211f34"/></linearGradient></defs>',
           '<style>@media(prefers-reduced-motion:no-preference){.scan{animation:scan 14s linear infinite}.lamp{animation:lamp 8s ease-in-out infinite}}@keyframes scan{0%{stroke-dashoffset:4;opacity:0}8%,85%{opacity:.85}100%{stroke-dashoffset:-100;opacity:0}}@keyframes lamp{0%,100%{opacity:.7}45%{opacity:1}}</style>',
           f'<rect width="{w}" height="{h}" rx="12" fill="url(#bg)"/>']
    out.append(label(f'{snapshot["total"]:,}',x,57,51,"#fff1d8",750,spacing=-2))
    digits = len(f'{snapshot["total"]:,}')
    metric_x = x + digits*29 + 9
    out.append(label("contributions",metric_x,53,23 if small else 28,"#f6eee6",700,spacing=-.5))
    dates = f"{date_label(days[0][0])} – {date_label(days[-1][0])}"
    out.append(label(dates,x if small else w-28,83 if small else 50,13 if small else 15,
                     "#bfd5d4",mono=True,anchor="start" if small else "end"))
    weeks = []
    for day, count in days:
        if not weeks or day.weekday() == 6:
            weeks.append([])
        weeks[-1].append((day,count))
    if small:
        split = (len(weeks)+1)//2
        out.append(calendar_strip(weeks[:split],36,124,w-53,True))
        out.append(calendar_strip(weeks[split:],36,260,w-53,True))
        legend_y, title_y, row_y = 380, 425, 457
    else:
        out.append(calendar_strip(weeks,58,103,w-100,False))
        legend_y, title_y, row_y = 215, 256, 284
    out.append(label("Daily count",x,legend_y,13,"#d1dbe4",650))
    for i,item in enumerate(LEGEND):
        offset=x+(92 if small else 112)+i*(53 if small else 63)
        out.append(cell(offset,legend_y-9,[0,1,2,4,7][i],8))
        out.append(label(item,offset+14,legend_y,12,"#d9e1ed",mono=True))
    out.append(line(f"M{x} {title_y-25}H{w-x}","#48596b",.8))
    out.append(label(title,x,title_y,22,"#f5e9d5",700,spacing=-.4))
    if not timeline:
        out.append(label("No active days in this period.",x,row_y+12,15,"#ced8e4"))
    for i,(day,verb,repo) in enumerate(timeline):
        xx = x if small else x+i*279
        yy = row_y+i*47 if small else row_y
        color = ("#81e2c6","#bba6f3","#f5b797")[i]
        if small and i < len(timeline)-1:
            out.append(line(f"M{xx+4} {yy+3}v35","#53677b"))
        out.append(f'<circle cx="{xx+4}" cy="{yy-2}" r="4" fill="{color}"/>')
        out.append(label(day.strftime("%d %b"),xx+15,yy+2,12,color,650,mono=True))
        out.append(label(verb,xx+(82 if small else 15),yy+(3 if small else 22),15,"#f3eff2",650))
        if repo:
            short = repo.split("/",1)[1] if repo.lower().startswith(owner.lower()+"/") else repo
            display = short if len(short)<=29 else short[:27]+"…"
            out.append(label(display,xx+(82 if small else 15), yy+(21 if small else 42),12,"#c3cfdf",mono=True))
    out.append("</svg>\n")
    return "".join(out)


def save(owner, snapshot, target):
    days = verified_days(snapshot)
    title, items = recent_activity(owner, snapshot.get("events", []), days)
    target.mkdir(parents=True, exist_ok=True)
    for mobile, name in [(False,"activity.svg"),(True,"activity-mobile.svg")]:
        svg = render(owner,snapshot,mobile)
        (target/name).write_text(svg,encoding="utf-8")
        (target/name.replace(".svg","-still.svg")).write_text(re.sub(r"<style>.*?</style>","",svg),encoding="utf-8")
    summary = ["# GitHub contribution activity", "",
               f'{snapshot["total"]:,} contributions from {date_label(days[0][0])} through {date_label(days[-1][0])}.',
               "", "## " + title, ""]
    for day, verb, repo in items:
        link = f" · [{repo}](https://github.com/{repo})" if repo else ""
        summary.append(f"- {date_label(day)} · {verb}{link}")
    if not items:
        summary.append("No active days in this period.")
    summary += ["", "## Daily counts", "", "<details><summary>Dates with contributions</summary>", ""]
    summary += [f"- {day.isoformat()} · {n}" for day,n in reversed(days) if n]
    summary += ["", "</details>", ""]
    (target/"activity-summary.md").write_text("\n".join(summary),encoding="utf-8")


if __name__ == "__main__":
    owner = os.environ["GITHUB_REPOSITORY_OWNER"]
    target = Path(sys.argv[1])
    save(owner, read_activity(owner, os.environ["GITHUB_TOKEN"]), target)
