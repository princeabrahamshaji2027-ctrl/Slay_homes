import React, { useRef } from 'react';
import { motion, useScroll, useTransform } from 'framer-motion';

const RevealText = ({ children }) => {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start 90%", "end 50%"]
  });

  const opacity = useTransform(scrollYProgress, [0, 1], [0.1, 1]);
  const scale = useTransform(scrollYProgress, [0, 1], [0.95, 1]);

  return (
    <motion.p 
      ref={ref}
      style={{ opacity, scale }}
      className="text-5xl md:text-8xl font-black tracking-tight leading-none mb-16 text-white text-center"
    >
      {children}
    </motion.p>
  );
};

const TextRevealSection = () => {
  return (
    <div className="py-64 px-4 bg-[#0b0b0f] min-h-screen flex flex-col justify-center">
      <div className="max-w-7xl mx-auto">
        <RevealText>Imagine a service that understands your needs.</RevealText>
        <RevealText>A system built for reliability.</RevealText>
        <RevealText>Every interaction designed to feel effortless.</RevealText>
        <RevealText>This is not just delivery.</RevealText>
        <RevealText>This is experience.</RevealText>
      </div>
    </div>
  );
};

export default TextRevealSection;
