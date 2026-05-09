import React from 'react';
import { motion } from 'framer-motion';

const Testimonial = ({ name, role, quote }) => (
  <motion.div 
    initial={{ opacity: 0, y: 30 }}
    whileInView={{ opacity: 1, y: 0 }}
    viewport={{ once: true }}
    className="bg-white/5 backdrop-blur-2xl p-10 rounded-[40px] border border-white/10 hover:border-white/20 transition-all group"
  >
    <div className="flex items-center gap-4 mb-8">
      <div className="w-14 h-14 rounded-full bg-gradient-to-tr from-white/20 to-white/5 flex items-center justify-center text-xl font-bold text-white">
        {name[0]}
      </div>
      <div>
        <h4 className="text-xl font-bold text-white">{name}</h4>
        <p className="text-sm text-gray-400">{role}</p>
      </div>
    </div>
    <p className="text-2xl text-gray-300 italic font-medium leading-relaxed group-hover:text-white transition-colors">"{quote}"</p>
  </motion.div>
);

const TestimonialsSection = () => {
  const testimonials = [
    { name: "Sarah J.", role: "Smart Home Owner", quote: "The most seamless integration I've ever experienced. Everything just works." },
    { name: "Michael R.", role: "Property Manager", quote: "SLAYHOMES changed how we manage our entire portfolio. 24/7 reliability is key." },
    { name: "David K.", role: "Architect", quote: "Clean, minimal, and premium. The hardware is just as good as the software." }
  ];

  return (
    <div className="py-64 bg-[#0b0b0f] px-4">
      <div className="max-w-7xl mx-auto">
        <h2 className="text-4xl md:text-6xl font-black text-center text-white mb-24 tracking-tighter">Trusted by Visionaries.</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
          {testimonials.map((t, i) => (
            <Testimonial key={i} {...t} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default TestimonialsSection;
