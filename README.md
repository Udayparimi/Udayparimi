<a href="https://udayparimi.github.io/Udayparimi/project-explorer.html#display" title="Try the interactive flip-dot display"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="docs/flipdot/display-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="docs/flipdot/display-still.svg"><source media="(max-width: 600px)" srcset="docs/flipdot/display-mobile.svg"><img width="100%" src="docs/flipdot/display.svg" alt="Udaya Raghavendra, data analytics and full-stack development. A 19-by-7 flip-dot display turns from JSX to Python to SQL."></picture></a>

<picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="docs/folio/about-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/about-still.svg"><source media="(max-width: 600px)" srcset="docs/folio/about-mobile.svg"><img src="docs/folio/about.svg" width="100%" alt="I’m Uday. I compare forecasting and churn models in Python and build web apps for payments and campus events. My goal is a data analyst role. First-year MCA at CHRIST (Deemed to be University), Bengaluru. BCA in Data Science from Acharya Institute of Graduate Studies, Bengaluru, 2023–2026."></picture>

<p><a href="#jump-data-analysis"><img src="docs/folio/nav-data-analysis.svg" alt="Data analysis"></a> <a href="#jump-web-applications"><img src="docs/folio/nav-web-applications.svg" alt="Web applications"></a> <a href="#jump-build-archive"><img src="docs/folio/nav-build-archive.svg" alt="Build archive"></a> <a href="#jump-skills"><img src="docs/folio/nav-skills.svg" alt="Skills"></a> <a href="#jump-contact"><img src="docs/folio/nav-contact.svg" alt="Contact"></a></p>

<a name="jump-data-analysis"></a>

## <picture><source media="(prefers-color-scheme: dark)" srcset="docs/flipdot/data-analysis-dark.svg"><img src="docs/flipdot/data-analysis-light.svg" alt="Data analysis"></picture>

<a href="https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-forecast" title="Inspect Sales Forecasting in 3D"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="docs/folio/forecast-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/forecast-still.svg"><source media="(max-width: 600px)" srcset="docs/folio/forecast-mobile.svg"><img src="docs/folio/forecast.svg" width="100%" alt="Sales Forecasting. Three models on a 90-day holdout. Prophet recorded the lowest error. 90-day holdout."></picture></a>

<details>
<summary><strong>Inside Sales Forecasting</strong></summary>

On daily grocery sales, Prophet returned a mean absolute error of 74k. SARIMAX and LSTM each returned 99k.

**90-day holdout**

```text
Prophet · MAE 74k · RMSE 100k
```

SARIMAX · Prophet · LSTM  
[Repository ↗](https://github.com/Udayparimi/sales-forecasting-arima-prophet-lstm) · [Inspect in 3D ↗](https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-forecast)

</details>

<a href="https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-churn" title="Inspect Customer Churn Prediction in 3D"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="docs/folio/churn-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/churn-still.svg"><source media="(max-width: 600px)" srcset="docs/folio/churn-mobile.svg"><img src="docs/folio/churn.svg" width="100%" alt="Customer Churn Prediction. Contract, tenure and monthly charges feed three Telco churn classifiers. Telco customer features."></picture></a>

<details>
<summary><strong>Inside Customer Churn Prediction</strong></summary>

The notebook compares logistic regression, random forest, and XGBoost and examines contract type, tenure, and monthly charges.

**Telco customer features**

```text
Contract type · tenure · monthly charges
```

Python · logistic regression · random forest · XGBoost  
[Repository ↗](https://github.com/Udayparimi/customer-churn-prediction) · [Inspect in 3D ↗](https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-churn)

</details>

<a name="jump-web-applications"></a>

## <picture><source media="(prefers-color-scheme: dark)" srcset="docs/flipdot/web-applications-dark.svg"><img src="docs/flipdot/web-applications-light.svg" alt="Web applications"></picture>

<p>
<a href="https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-hotel" title="Inspect Hotel Payment Tracker in 3D"><picture><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/hotel-still.svg"><img src="docs/folio/hotel.svg" width="411" alt="Hotel Payment Tracker. Next.js fetches reports on the server. The payments client handles edits. Client handoff."></picture></a>
<a href="https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-campus" title="Inspect Campus Event Management in 3D"><picture><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/campus-still.svg"><img src="docs/folio/campus.svg" width="411" alt="Campus Event Management. A verified JWT routes students to registration and admins to event tools. Student permission."></picture></a>
</p>

<details>
<summary><strong>Inside Hotel Payment Tracker</strong></summary>

Reports fetch payment data on the server. The payments page hands the initial list to a client component for search, filtering, and edits.

**Client handoff**

```text
PaymentsClient.jsx
```

Next.js · React · Express · MongoDB  
[Repository ↗](https://github.com/Udayparimi/FSD-Lab9-10) · [Inspect in 3D ↗](https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-hotel)

</details>

<details>
<summary><strong>Inside Campus Event Management</strong></summary>

Students register for events while admins manage the event lifecycle through role-protected routes.

**Student permission**

```text
student → register for event
```

MERN · JWT · React Router  
[Repository ↗](https://github.com/Udayparimi/Campus-event-management) · [Inspect in 3D ↗](https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-campus)

</details>

<p>
<a href="https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-student" title="Inspect Student Project Tracker in 3D"><picture><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/student-still.svg"><img src="docs/folio/student.svg" width="411" alt="Student Project Tracker. A status change sends an update to Express and refreshes the list. Status update."></picture></a>
<a href="https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-dashboard" title="Inspect Payment Tracking Dashboard in 3D"><picture><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/dashboard-still.svg"><img src="docs/folio/dashboard.svg" width="411" alt="Payment Tracking Dashboard. Filter stored payments by method and review matching records. Method filter."></picture></a>
</p>

<details>
<summary><strong>Inside Student Project Tracker</strong></summary>

The React form adds projects. Changing a status sends a PUT request with projectStatus and fetches the refreshed list.

**Status update**

```text
PUT /projects/:id
{ "projectStatus": "ongoing" }
```

React · Express · MongoDB  
[Repository ↗](https://github.com/Udayparimi/FSD-CIA-3) · [Inspect in 3D ↗](https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-student)

</details>

<details>
<summary><strong>Inside Payment Tracking Dashboard</strong></summary>

The dashboard searches and filters payment records, calculates revenue statistics, and persists changes in browser storage.

**Method filter**

```text
payment.method === selected
```

JavaScript · Local Storage API  
[Repository ↗](https://github.com/Udayparimi/Payment-Tracking-dashboard) · [Inspect in 3D ↗](https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-dashboard)

</details>

<a name="jump-build-archive"></a>

## <picture><source media="(prefers-color-scheme: dark)" srcset="docs/flipdot/build-archive-dark.svg"><img src="docs/flipdot/build-archive-light.svg" alt="Build archive"></picture>

### <img src="docs/folio/archive-browser.svg" alt="Browser and storage">

<a href="https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-hotel-static" title="Inspect Responsive Hotel Pages in 3D"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="docs/folio/hotel-static-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/hotel-static-still.svg"><source media="(max-width: 600px)" srcset="docs/folio/hotel-static-mobile.svg"><img src="docs/folio/hotel-static.svg" width="100%" alt="Responsive Hotel Pages. Payment pages reflow from a wide layout into a single mobile column. Responsive layout."></picture></a>

<details>
<summary><strong>Inside Responsive Hotel Pages</strong></summary>

Responsive pages cover payments, reports, analytics, and hotel navigation.

**Responsive layout**

```text
Wide viewport → narrow viewport
```

HTML · CSS  
[Repository ↗](https://github.com/Udayparimi/hotel-payment-tracking-system) · [Inspect in 3D ↗](https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-hotel-static)

</details>

<a href="https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-hotel-local" title="Inspect Browser Payment Storage in 3D"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="docs/folio/hotel-local-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/hotel-local-still.svg"><source media="(max-width: 600px)" srcset="docs/folio/hotel-local-mobile.svg"><img src="docs/folio/hotel-local.svg" width="100%" alt="Browser Payment Storage. Write a payment record to localStorage and retrieve it on the next visit. Browser write."></picture></a>

<details>
<summary><strong>Inside Browser Payment Storage</strong></summary>

A payment modal adds records and the browser keeps them under the payments key.

**Browser write**

```text
localStorage.setItem("payments", …)
```

JavaScript · Local Storage API  
[Repository ↗](https://github.com/Udayparimi/Hotel-Payment-Tracker-Lab2) · [Inspect in 3D ↗](https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-hotel-local)

</details>

<a href="https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-hotel-register" title="Inspect Guest Registration in 3D"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="docs/folio/hotel-register-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/hotel-register-still.svg"><source media="(max-width: 600px)" srcset="docs/folio/hotel-register-mobile.svg"><img src="docs/folio/hotel-register.svg" width="100%" alt="Guest Registration. Validate guest details, then generate a customer ID and temporary PIN. After validation."></picture></a>

<details>
<summary><strong>Inside Guest Registration</strong></summary>

The registration module validates input, generates a customer ID and temporary PIN, and stores the customer locally.

**After validation**

```text
Customer ID + temporary PIN
```

JavaScript · form validation · localStorage  
[Repository ↗](https://github.com/Udayparimi/Hotel-Payment-Tracker-Lab3) · [Inspect in 3D ↗](https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-hotel-register)

</details>

<a href="https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-hotel-crud" title="Inspect Payment CRUD in 3D"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="docs/folio/hotel-crud-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/hotel-crud-still.svg"><source media="(max-width: 600px)" srcset="docs/folio/hotel-crud-mobile.svg"><img src="docs/folio/hotel-crud.svg" width="100%" alt="Payment CRUD. Editing a stored payment changes the status used in the reports. Record change."></picture></a>

<details>
<summary><strong>Inside Payment CRUD</strong></summary>

Updates to stored payment objects change the paid and pending categories in the reports.

**Record change**

```text
status: "Pending" → "Paid"
```

JavaScript · CRUD · localStorage  
[Repository ↗](https://github.com/Udayparimi/Hotel-Payment-Tracker-Lab4) · [Inspect in 3D ↗](https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-hotel-crud)

</details>

### <img src="docs/folio/archive-services.svg" alt="Application services">

<a href="https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-hotel-api" title="Inspect Hotel Payments REST API in 3D"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="docs/folio/hotel-api-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/hotel-api-still.svg"><source media="(max-width: 600px)" srcset="docs/folio/hotel-api-mobile.svg"><img src="docs/folio/hotel-api.svg" width="100%" alt="Hotel Payments REST API. Follow a payment lookup through Express and MongoDB to the response. HTTP request."></picture></a>

<details>
<summary><strong>Inside Hotel Payments REST API</strong></summary>

The Express API exposes CRUD endpoints for payments and registrations. The diagram follows GET /api/payments/:id.

**HTTP request**

```text
GET /api/payments/:id
```

Node.js · Express · Mongoose · MongoDB  
[Repository ↗](https://github.com/Udayparimi/FSD-Lab4) · [Inspect in 3D ↗](https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-hotel-api)

</details>

<a href="https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-hotel-mern" title="Inspect HotelPay MERN Build in 3D"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="docs/folio/hotel-mern-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/hotel-mern-still.svg"><source media="(max-width: 600px)" srcset="docs/folio/hotel-mern-mobile.svg"><img src="docs/folio/hotel-mern.svg" width="100%" alt="HotelPay MERN Build. The Vite client talks to an Express API backed by MongoDB. Request path."></picture></a>

<details>
<summary><strong>Inside HotelPay MERN Build</strong></summary>

HotelPay runs a React frontend and an Express backend with a configurable MongoDB connection.

**Request path**

```text
React → Express → MongoDB
```

React · Vite · Express · MongoDB  
[Repository ↗](https://github.com/Udayparimi/FSD-Lab5-and-6) · [Inspect in 3D ↗](https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-hotel-mern)

</details>

<a href="https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-hotel-reactlab" title="Inspect React Hotel Tracker in 3D"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="docs/folio/hotel-reactlab-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/hotel-reactlab-still.svg"><source media="(max-width: 600px)" srcset="docs/folio/hotel-reactlab-mobile.svg"><img src="docs/folio/hotel-reactlab.svg" width="100%" alt="React Hotel Tracker. Local page state selects which React component is mounted. Active component."></picture></a>

<details>
<summary><strong>Inside React Hotel Tracker</strong></summary>

App.jsx switches between Registration, Payments, and ActivityLog based on local page state.

**Active component**

```text
setPage("payments") → <Payments />
```

React · useState · JSX  
[Repository ↗](https://github.com/Udayparimi/hotel-payment-tracker-Lab7) · [Inspect in 3D ↗](https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-hotel-reactlab)

</details>

<a href="https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-hotel-mail" title="Inspect Payment Receipt Email in 3D"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="docs/folio/hotel-mail-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/hotel-mail-still.svg"><source media="(max-width: 600px)" srcset="docs/folio/hotel-mail-mobile.svg"><img src="docs/folio/hotel-mail.svg" width="100%" alt="Payment Receipt Email. A paid payment can send a receipt when SMTP is configured. Delivery condition."></picture></a>

<details>
<summary><strong>Inside Payment Receipt Email</strong></summary>

When SMTP is configured, the backend can send a receipt for a paid payment. The API also runs without mail configuration.

**Delivery condition**

```text
Paid payment + configured SMTP → receipt
```

Express · MongoDB · Nodemailer  
[Repository ↗](https://github.com/Udayparimi/FSD-Lab8) · [Inspect in 3D ↗](https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-hotel-mail)

</details>

### <img src="docs/folio/archive-routing.svg" alt="Routing and check-in">

<a href="https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-hotel-router" title="Inspect React Router Hotel Pages in 3D"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="docs/folio/hotel-router-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/hotel-router-still.svg"><source media="(max-width: 600px)" srcset="docs/folio/hotel-router-mobile.svg"><img src="docs/folio/hotel-router.svg" width="100%" alt="React Router Hotel Pages. An address change selects the view inside the same React application. Route match."></picture></a>

<details>
<summary><strong>Inside React Router Hotel Pages</strong></summary>

React Router replaces separate HTML pages with client-side routes while API calls are centralized in src/api.js.

**Route match**

```text
/analytics → Analytics.jsx
```

React · Vite · React Router  
[Repository ↗](https://github.com/Udayparimi/FSD-Lab08) · [Inspect in 3D ↗](https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-hotel-router)

</details>

<a href="https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-campus-ete" title="Inspect Campus Pass Verification in 3D"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="docs/folio/campus-ete-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/campus-ete-still.svg"><source media="(max-width: 600px)" srcset="docs/folio/campus-ete-mobile.svg"><img src="docs/folio/campus-ete.svg" width="100%" alt="Campus Pass Verification. An admin looks up a ticket code and checks in a registered guest. Verification route."></picture></a>

<details>
<summary><strong>Inside Campus Pass Verification</strong></summary>

Confirmed registrations receive a ticket code and QR pass. Admins can verify the code and check the student in. The preview QR opens this repository.

**Verification route**

```text
/verify-pass → ticket lookup → check-in
```

MERN · JWT · QR passes  
[Repository ↗](https://github.com/Udayparimi/FSD-ETE) · [Inspect in 3D ↗](https://udayparimi.github.io/Udayparimi/project-explorer.html#inspect-campus-ete)

</details>

<a name="jump-skills"></a>

## <picture><source media="(prefers-color-scheme: dark)" srcset="docs/flipdot/skills-dark.svg"><img src="docs/flipdot/skills-light.svg" alt="Skills"></picture>

<p>
<a href="https://github.com/Udayparimi/customer-churn-prediction"><picture><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/skill-languages-still.svg"><img src="docs/folio/skill-languages.svg" width="411" alt="Python, SQL, JavaScript and C, including data structures."></picture></a>
<a href="https://github.com/Udayparimi/FSD-Lab9-10"><picture><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/skill-web-still.svg"><img src="docs/folio/skill-web.svg" width="411" alt="Full-stack web development with React, Next.js, Express and Node.js."></picture></a>
</p>

<p>
<a href="https://github.com/Udayparimi/sales-forecasting-arima-prophet-lstm"><picture><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/skill-data-still.svg"><img src="docs/folio/skill-data.svg" width="411" alt="Data tools and databases include Pandas, Prophet, SARIMAX, LSTM, MongoDB, MySQL and Oracle."></picture></a>
<a href="https://github.com/Udayparimi/FSD-Lab5-and-6"><picture><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/skill-tools-still.svg"><img src="docs/folio/skill-tools.svg" width="411" alt="Jupyter Notebook, Vite and GitHub."></picture></a>
</p>

<details class="plain-profile"><summary>Bio, education and skills in text</summary><p>I’m Uday. I compare forecasting and churn models in Python and build web apps for payments and campus events. My goal is a data analyst role.</p><p>First-year MCA at CHRIST (Deemed to be University), Bengaluru. BCA in Data Science from Acharya Institute of Graduate Studies, Bengaluru, 2023–2026.</p><ul><li><strong>Languages</strong> · Python · SQL · JavaScript · C · data structures</li><li><strong>Web</strong> · React · Next.js · Express · Node.js</li><li><strong>Data and databases</strong> · Pandas · Prophet · SARIMAX · LSTM · MongoDB · MySQL · Oracle</li><li><strong>Tools</strong> · Jupyter Notebook · Vite · GitHub</li></ul></details>

<a name="jump-contact"></a>

## <picture><source media="(prefers-color-scheme: dark)" srcset="docs/flipdot/contact-dark.svg"><img src="docs/flipdot/contact-light.svg" alt="Contact"></picture>

<p>
<a href="https://www.linkedin.com/in/udaya-raghavendra-9a846137b/"><picture><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/contact-linkedin-still.svg"><img src="docs/folio/contact-linkedin.svg" width="411" alt="LinkedIn — open Uday’s profile"></picture></a>
<a href="https://github.com/Udayparimi?tab=repositories"><picture><source media="(prefers-reduced-motion: reduce)" srcset="docs/folio/contact-github-still.svg"><img src="docs/folio/contact-github.svg" width="411" alt="GitHub — browse Uday’s repositories"></picture></a>
</p>

<a name="jump-pinned-projects"></a>

## <picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/index-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/index-still.svg"><source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/index-mobile.svg"><img src="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/index.svg" alt="Pinned projects" width="100%"></picture>

<p>
<a href="https://github.com/Udayparimi/customer-churn-prediction"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/churn-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/churn-still.svg"><source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/churn-mobile.svg"><img src="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/churn.svg" alt="Customer churn. Compare three classifiers on Telco customer data. Python · XGBoost. Open customer-churn-prediction." width="100%"></picture></a><br>
<a href="https://github.com/Udayparimi/sales-forecasting-arima-prophet-lstm"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/forecast-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/forecast-still.svg"><source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/forecast-mobile.svg"><img src="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/forecast.svg" alt="Sales forecasting. Compare grocery forecasts on a 90-day holdout. Prophet · SARIMAX · LSTM. Open sales-forecasting-arima-prophet-lstm." width="100%"></picture></a><br>
<a href="https://github.com/Udayparimi/Campus-event-management"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/campus-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/campus-still.svg"><source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/campus-mobile.svg"><img src="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/campus.svg" alt="Campus events. Student registration and admin tools. React · Express · JWT. Open Campus-event-management." width="100%"></picture></a><br>
<a href="https://github.com/Udayparimi/FSD-CIA-3"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/student-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/student-still.svg"><source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/student-mobile.svg"><img src="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/student.svg" alt="Student project tracker. Track projects from proposal to completion. React · Express · MongoDB. Open FSD-CIA-3." width="100%"></picture></a><br>
<a href="https://github.com/Udayparimi/FSD-Lab5-and-6"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/hotel-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/hotel-still.svg"><source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/hotel-mobile.svg"><img src="https://raw.githubusercontent.com/Udayparimi/Udayparimi/main/docs/pins/hotel.svg" alt="HotelPay. Hotel payments and bookings. React · Express · MongoDB. Open FSD-Lab5-and-6." width="100%"></picture></a>
</p>

<a name="jump-github-activity"></a>

## <picture><source media="(prefers-color-scheme: dark)" srcset="docs/flipdot/github-activity-dark.svg"><img src="docs/flipdot/github-activity-light.svg" alt="GitHub activity"></picture>

<a href="https://github.com/Udayparimi/Udayparimi/blob/output/activity-summary.md"><picture><source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/output/activity-mobile-still.svg"><source media="(prefers-reduced-motion: reduce)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/output/activity-still.svg"><source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/Udayparimi/Udayparimi/output/activity-mobile.svg"><img src="https://raw.githubusercontent.com/Udayparimi/Udayparimi/output/activity.svg" alt="GitHub contribution counts by day and recent activity. Open the text summary for dates and counts." width="100%"></picture></a>

[Activity in text](https://github.com/Udayparimi/Udayparimi/blob/output/activity-summary.md) · [GitHub’s daily counts](https://github.com/users/Udayparimi/contributions)

<details>
<summary><strong>Stats, languages, streak and contribution calendar</strong></summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=Udayparimi&amp;hide_border=true&amp;show_icons=true&amp;theme=github_dark&amp;title_color=ffbc90&amp;text_color=d8e5ff&amp;icon_color=a5f3db&amp;bg_color=211d30">
  <img src="https://github-readme-stats.vercel.app/api?username=Udayparimi&amp;hide_border=true&amp;show_icons=true&amp;theme=default" alt="GitHub activity statistics">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=Udayparimi&amp;layout=compact&amp;hide_border=true&amp;theme=github_dark&amp;title_color=ffbc90&amp;text_color=d8e5ff&amp;icon_color=a5f3db&amp;bg_color=211d30">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Udayparimi&amp;layout=compact&amp;hide_border=true&amp;theme=default" alt="Most used repository languages">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com/?user=Udayparimi&amp;theme=github-dark-blue&amp;background=211d30&amp;ring=a5f3db&amp;fire=ffbc90&amp;currStreakLabel=ffbc90&amp;hide_border=true">
  <img src="https://streak-stats.demolab.com/?user=Udayparimi&amp;theme=default&amp;hide_border=true" alt="GitHub contribution streak">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/Udayparimi/Udayparimi/raw/refs/heads/output/snake-dark.svg">
  <img src="https://github.com/Udayparimi/Udayparimi/raw/refs/heads/output/snake-light.svg" alt="Animated contribution snake">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/Udayparimi/Udayparimi/raw/refs/heads/output/calendar-dark.svg">
  <img src="https://github.com/Udayparimi/Udayparimi/raw/refs/heads/output/calendar-light.svg" alt="3D GitHub contribution calendar">
</picture>


[View contributions on GitHub](https://github.com/Udayparimi)

</details>
