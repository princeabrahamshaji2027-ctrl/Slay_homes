import React from 'react';
import HeroScrollSection from './components/HeroScrollSection';
import FeatureStorySection from './components/FeatureStorySection';
import TextRevealSection from './components/TextRevealSection';
import TestimonialsSection from './components/TestimonialsSection';

function App() {
  return (
    <div className="bg-[#0b0b0f] text-white w-full">
      <HeroScrollSection />
      <FeatureStorySection />
      <TextRevealSection />
      <TestimonialsSection />
    </div>
  );
}

export default App;
