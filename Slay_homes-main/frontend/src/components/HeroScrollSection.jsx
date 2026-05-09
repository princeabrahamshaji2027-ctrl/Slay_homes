import React, { useState, useEffect, useRef, useCallback, useMemo } from 'react';
import { motion, useScroll, useTransform, useMotionValueEvent, useSpring } from 'framer-motion';

const TOTAL_FRAMES = 240;

const HeroScrollSection = () => {
  const containerRef = useRef(null);
  const canvasRef = useRef(null);
  const imagesRef = useRef([]);
  const [imagesLoaded, setImagesLoaded] = useState(false);
  const [loadedCount, setLoadedCount] = useState(0);

  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ["start start", "end end"]
  });

  // Smooth the scroll progress for less jittery animation
  const smoothScrollY = useSpring(scrollYProgress, {
    stiffness: 100,
    damping: 30,
    restDelta: 0.001
  });

  const frameIndex = useTransform(smoothScrollY, [0, 0.8], [1, TOTAL_FRAMES]);

  const drawFrame = useCallback((index) => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d', { alpha: false }); // Optimization: disable alpha
    const img = imagesRef.current[index];
    
    if (img && img.complete) {
      const canvasWidth = window.innerWidth;
      const canvasHeight = window.innerHeight;
      
      if (canvas.width !== canvasWidth || canvas.height !== canvasHeight) {
        canvas.width = canvasWidth;
        canvas.height = canvasHeight;
      }
      
      const canvasRatio = canvas.width / canvas.height;
      const imgRatio = img.width / img.height;
      let drawWidth = canvas.width;
      let drawHeight = canvas.height;
      let offsetX = 0;
      let offsetY = 0;

      if (canvasRatio > imgRatio) {
        drawHeight = canvas.width / imgRatio;
        offsetY = (canvas.height - drawHeight) / 2;
      } else {
        drawWidth = canvas.height * imgRatio;
        offsetX = (canvas.width - drawWidth) / 2;
      }

      ctx.drawImage(img, offsetX, offsetY, drawWidth, drawHeight);
    }
  }, []);

  useEffect(() => {
    let loaded = 0;
    const loadImages = async () => {
      for (let i = 1; i <= TOTAL_FRAMES; i++) {
        const img = new Image();
        const paddedIndex = i.toString().padStart(3, '0');
        img.src = `/static/ezgif-frame-${paddedIndex}.jpg`;
        img.onload = () => {
          imagesRef.current[i] = img;
          loaded++;
          setLoadedCount(loaded);
          if (loaded === TOTAL_FRAMES) {
            setImagesLoaded(true);
            drawFrame(1);
          }
        };
        img.onerror = () => {
          loaded++;
          setLoadedCount(loaded);
          if (loaded === TOTAL_FRAMES) setImagesLoaded(true);
        };
      }
    };
    loadImages();

    const handleResize = () => drawFrame(Math.round(frameIndex.get()));
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, [drawFrame]);

  useMotionValueEvent(frameIndex, "change", (latest) => {
    if (imagesLoaded) {
      const index = Math.max(1, Math.min(TOTAL_FRAMES, Math.round(latest)));
      drawFrame(index);
    }
  });

  // Text animations based on scroll progress
  const textOpacity1 = useTransform(smoothScrollY, [0, 0.1, 0.15, 0.25], [0, 1, 1, 0]);
  const textY1 = useTransform(smoothScrollY, [0, 0.1, 0.15, 0.25], [50, 0, 0, -50]);

  const textOpacity2 = useTransform(smoothScrollY, [0.3, 0.4, 0.45, 0.55], [0, 1, 1, 0]);
  const textY2 = useTransform(smoothScrollY, [0.3, 0.4, 0.45, 0.55], [50, 0, 0, -50]);

  const textOpacity3 = useTransform(smoothScrollY, [0.6, 0.7, 0.75, 0.85], [0, 1, 1, 0]);
  const textY3 = useTransform(smoothScrollY, [0.6, 0.7, 0.75, 0.85], [50, 0, 0, -50]);

  return (
    <div ref={containerRef} className="relative w-full bg-[#0b0b0f]" style={{ height: '800vh' }}>
      {!imagesLoaded && (
        <div className="fixed inset-0 flex flex-col items-center justify-center z-[100] bg-[#0b0b0f]">
          <div className="w-64 h-1 bg-white/20 rounded-full overflow-hidden mb-4">
            <div className="h-full bg-white transition-all duration-300" style={{ width: `${(loadedCount / TOTAL_FRAMES) * 100}%` }}></div>
          </div>
          <p className="text-gray-400 text-sm font-medium tracking-widest uppercase">Initializing Cinematic Experience</p>
        </div>
      )}
      
      <div className="sticky top-0 w-full h-screen overflow-hidden flex items-center justify-center bg-[#0b0b0f]">
        <canvas 
          ref={canvasRef} 
          className="absolute inset-0 w-full h-full opacity-60 transition-opacity duration-1000"
          style={{ opacity: imagesLoaded ? 0.6 : 0 }}
        />
        
        <div className="absolute inset-0 bg-gradient-to-t from-[#0b0b0f] via-transparent to-[#0b0b0f]/80 pointer-events-none"></div>
        <div className="absolute inset-0 bg-black/40 pointer-events-none"></div>

        {/* Text Overlays synced with scroll */}
        <motion.div style={{ opacity: textOpacity1, y: textY1 }} className="absolute z-10 text-center">
            <h1 className="text-white text-6xl md:text-9xl font-black tracking-tighter mb-4">Comfort, Delivered.</h1>
            <p className="text-gray-400 text-2xl md:text-4xl font-medium">Luxury Meets Simplicity</p>
        </motion.div>

        <motion.div style={{ opacity: textOpacity2, y: textY2 }} className="absolute z-10 text-center">
            <h1 className="text-white text-6xl md:text-9xl font-black tracking-tighter mb-4">Your Space.</h1>
            <p className="text-gray-400 text-2xl md:text-4xl font-medium">Your Control.</p>
        </motion.div>

        <motion.div style={{ opacity: textOpacity3, y: textY3 }} className="absolute z-10 text-center">
            <h1 className="text-white text-6xl md:text-9xl font-black tracking-tighter mb-4">The Future.</h1>
            <p className="text-gray-400 text-2xl md:text-4xl font-medium">Right at Home</p>
        </motion.div>
      </div>

      {/* Feature Story Integrated into the flow */}
      <div className="relative z-20 mt-[-100vh]">
         {/* These will scroll naturally after the hero sticky part ends or during it */}
      </div>
    </div>
  );
};

export default HeroScrollSection;
