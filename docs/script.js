(() => {
  const carousel = document.querySelector(".carousel");
  const viewport = carousel?.querySelector(".viewport");
  const track = carousel?.querySelector(".track");
  const previous = carousel?.querySelector(".previous");
  const next = carousel?.querySelector(".next");
  const pause = carousel?.querySelector(".pause");
  const current = carousel?.querySelector(".current");
  const progress = carousel?.querySelector(".progress-fill");
  const status = carousel?.querySelector(".status");

  if (!carousel || !viewport || !track || !previous || !next || !pause) return;

  const originals = Array.from(track.children);
  const total = originals.length;
  const titles = originals.map((slide) => slide.querySelector("h2")?.textContent?.trim() || "");
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const lastClone = originals[total - 1].cloneNode(true);
  const firstClone = originals[0].cloneNode(true);

  lastClone.setAttribute("aria-hidden", "true");
  firstClone.setAttribute("aria-hidden", "true");
  lastClone.dataset.clone = "true";
  firstClone.dataset.clone = "true";
  track.prepend(lastClone);
  track.append(firstClone);

  let position = 1;
  let logicalIndex = 0;
  let timer = null;
  let autoplay = !reduceMotion.matches;
  let temporarilyPaused = false;
  let pointerStart = null;

  const setTransform = (animate = true) => {
    track.style.transition = animate ? "transform 720ms var(--ease)" : "none";
    track.style.transform = `translate3d(${-position * 100}%, 0, 0)`;
  };

  const updateInterface = () => {
    originals.forEach((slide, index) => {
      slide.setAttribute("aria-hidden", index === logicalIndex ? "false" : "true");
    });
    if (current) current.textContent = String(logicalIndex + 1).padStart(2, "0");
    if (progress) progress.style.transform = `scaleX(${(logicalIndex + 1) / total})`;
    if (status) status.textContent = `第 ${logicalIndex + 1} 张，共 ${total} 张：${titles[logicalIndex]}`;
  };

  const stopTimer = () => {
    if (timer !== null) window.clearInterval(timer);
    timer = null;
  };

  const startTimer = () => {
    stopTimer();
    if (!autoplay || temporarilyPaused || document.hidden) return;
    timer = window.setInterval(() => move(1, false), 4800);
  };

  const move = (step, userInitiated = true) => {
    position += step;
    logicalIndex = (logicalIndex + step + total) % total;
    setTransform(true);
    updateInterface();
    if (userInitiated) startTimer();
  };

  track.addEventListener("transitionend", () => {
    if (position === total + 1) {
      position = 1;
      setTransform(false);
    } else if (position === 0) {
      position = total;
      setTransform(false);
    }
  });

  previous.addEventListener("click", () => move(-1));
  next.addEventListener("click", () => move(1));

  pause.addEventListener("click", () => {
    autoplay = !autoplay;
    pause.textContent = autoplay ? "暂停" : "播放";
    pause.setAttribute("aria-label", autoplay ? "暂停自动播放" : "开始自动播放");
    pause.setAttribute("aria-pressed", String(!autoplay));
    startTimer();
  });

  viewport.addEventListener("keydown", (event) => {
    if (event.key === "ArrowLeft") {
      event.preventDefault();
      move(-1);
    }
    if (event.key === "ArrowRight") {
      event.preventDefault();
      move(1);
    }
  });

  viewport.addEventListener("pointerdown", (event) => {
    pointerStart = event.clientX;
  });

  viewport.addEventListener("pointerup", (event) => {
    if (pointerStart === null) return;
    const distance = event.clientX - pointerStart;
    pointerStart = null;
    if (Math.abs(distance) > 48) move(distance > 0 ? -1 : 1);
  });

  viewport.addEventListener("pointercancel", () => {
    pointerStart = null;
  });

  carousel.addEventListener("pointerenter", () => {
    temporarilyPaused = true;
    stopTimer();
  });

  carousel.addEventListener("pointerleave", () => {
    temporarilyPaused = false;
    startTimer();
  });

  carousel.addEventListener("focusin", () => {
    temporarilyPaused = true;
    stopTimer();
  });

  carousel.addEventListener("focusout", (event) => {
    if (carousel.contains(event.relatedTarget)) return;
    temporarilyPaused = false;
    startTimer();
  });

  document.addEventListener("visibilitychange", startTimer);

  reduceMotion.addEventListener("change", (event) => {
    autoplay = !event.matches;
    pause.textContent = autoplay ? "暂停" : "播放";
    pause.setAttribute("aria-label", autoplay ? "暂停自动播放" : "开始自动播放");
    pause.setAttribute("aria-pressed", String(!autoplay));
    startTimer();
  });

  setTransform(false);
  updateInterface();
  startTimer();
})();
