import React, { useRef } from 'react';
import { motion, useScroll, useTransform } from 'framer-motion';

const Feature = ({ title, description }) => {
  return (
    <div className="h-screen flex items-center justify-center relative overflow-hidden bg-[#0b0b0f]">
       <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-white/5 to-transparent opacity-50"></div>
       <div className="text-center px-4 max-w-5xl mx-auto z-10">
          <motion.h2 
            initial={{ opacity: 0, y: 50 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, ease: "easeOut" }}
            className="text-6xl md:text-9xl font-black tracking-tighter text-white mb-8"
          >
            {title}
          </motion.h2>
          <motion.p 
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.2, ease: "easeOut" }}
            className="text-2xl md:text-4xl text-gray-400 font-medium leading-relaxed"
          >
            {description}
          </motion.p>
       </div>
    </div>
  );
};

const FeatureStorySection = () => {
  const features = [
    { title: "Instant Ordering", description: "Get what you need without waiting. Our system ensures minimal delay and maximum efficiency." },
    { title: "Smart Delivery", description: "Simple interface. Zero confusion. Order in seconds." },
    { title: "24/7 Service", description: "Late night or early morning — we’re always active. Reliable every time." },
    { title: "Designed for Comfort", description: "Your space is personal. Any service entering it should respect that." }
  ];

  return (
    <div className="relative w-full">
      {features.map((feature, i) => (
        <Feature key={i} {...feature} />
      ))}
    </div>
  );
};

export default FeatureStorySection;
