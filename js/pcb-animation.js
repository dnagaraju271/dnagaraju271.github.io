/* Gentle PCB LED variation; the SVG and CSS provide the live signal paths. */
(() => {
  const start = () => {
    const scene = document.querySelector("#space .pcb-scene");
    if (!scene) return;
    const leds = [...scene.querySelectorAll(".pcb-led, .pcb-leds circle")];
    if (!leds.length || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    leds.forEach((led, i) => {
      const delay = ((i * 0.73) % 4.5).toFixed(2);
      const duration = (3.2 + (i % 5) * 0.46).toFixed(2);
      led.style.animationDelay = "-" + delay + "s";
      led.style.animationDuration = duration + "s";
    });
    // Keep the artwork decorative and never let it intercept portfolio clicks.
    scene.setAttribute("focusable", "false");
    scene.style.pointerEvents = "none";
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start, { once: true });
  else start();
})();