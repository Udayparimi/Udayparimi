const host = document.querySelector('#scene');
const button = document.querySelector('#motion');
const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)');
let started = false;
let paused = false;
let visible = true;
let renderer;
let scene;
let camera;
let group;
let frame = 0;
let previous = 0;

function render() {
  renderer.render(scene, camera);
}

function tick(time) {
  const delta = Math.min((time - (previous || time)) / 1000, .045);
  previous = time;
  group.rotation.y += delta * .37;
  group.rotation.x += delta * .15;
  render();
  frame = requestAnimationFrame(tick);
}

function syncMotion() {
  if (!renderer) return;
  cancelAnimationFrame(frame);
  previous = 0;
  button.hidden = reduceMotion.matches;
  button.textContent = paused ? 'Resume 3D motion' : 'Pause 3D motion';
  if (!paused && visible && !document.hidden && !reduceMotion.matches) {
    frame = requestAnimationFrame(tick);
  } else {
    render();
  }
}

async function start() {
  if (started || reduceMotion.matches) return;
  started = true;
  try {
    const T = await import('https://cdn.jsdelivr.net/npm/three@0.179.1/build/three.module.js');
    if (reduceMotion.matches) {
      started = false;
      return;
    }
    renderer = new T.WebGLRenderer({alpha:true,antialias:true,powerPreference:'low-power'});
    renderer.setPixelRatio(Math.min(devicePixelRatio, 1.5));
    scene = new T.Scene();
    camera = new T.PerspectiveCamera(36,1,.1,40);
    camera.position.z = 7.8;
    group = new T.Group();
    group.rotation.set(.28,.48,.13);
    scene.add(group);
    const core = new T.IcosahedronGeometry(1.04,1);
    const shell = new T.IcosahedronGeometry(1.37,0);
    for (const [geometry,color,opacity] of [[core,0x6fe9ff,.78],[shell,0xb69cff,.5]]) {
      group.add(new T.LineSegments(new T.WireframeGeometry(geometry),new T.LineBasicMaterial({color,transparent:true,opacity})));
      geometry.dispose();
    }
    for (let i=0; i<3; i++) {
      const ring = new T.Mesh(new T.TorusGeometry(1.73+i*.105,.009,4,80),new T.MeshBasicMaterial({color:i===1?0xb69cff:0x6fe9ff,transparent:true,opacity:.58}));
      ring.rotation.set(.52+i*.71,.35+i*.37,-.2+i*.71);
      group.add(ring);
      const dot = new T.Mesh(new T.SphereGeometry(.05,10,8),new T.MeshBasicMaterial({color:i===1?0xcfb5ff:0xa4f3ff}));
      const angle = i*2.2;
      dot.position.set(Math.cos(angle)*(1.73+i*.105),Math.sin(angle)*(1.73+i*.105),0);
      ring.add(dot);
    }
    const resize = () => {
      const width = host.clientWidth;
      const height = host.clientHeight;
      if (!width || !height) return;
      camera.aspect = width / height;
      camera.fov = matchMedia('(max-width:680px)').matches ? 41 : 36;
      camera.position.x = matchMedia('(max-width:680px)').matches ? 0 : -1.15;
      camera.updateProjectionMatrix();
      renderer.setSize(width,height,false);
      render();
    };
    host.append(renderer.domElement);
    renderer.domElement.addEventListener('webglcontextlost', () => {
      cancelAnimationFrame(frame);
      renderer.domElement.remove();
      renderer = undefined;
      host.classList.remove('ready');
      button.hidden = true;
    });
    resize();
    host.classList.add('ready');
    new ResizeObserver(() => { if (renderer) resize(); }).observe(host);
    new IntersectionObserver(entries => {
      visible = entries[0].isIntersecting;
      syncMotion();
    }).observe(host);
    syncMotion();
  } catch {
    button.hidden = true;
  }
}

button.addEventListener('click', () => {
  paused = !paused;
  syncMotion();
});
document.addEventListener('visibilitychange',syncMotion);
reduceMotion.addEventListener('change',() => {
  if (renderer) syncMotion();
  else if (!reduceMotion.matches) start();
});
if ('requestIdleCallback' in window) requestIdleCallback(start,{timeout:1400});
else setTimeout(start,200);
