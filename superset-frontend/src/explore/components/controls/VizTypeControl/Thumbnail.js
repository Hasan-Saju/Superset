import React, { useState } from 'react';
import GanttChart from './GanttChart';

const ThumbnailGantt = ({ imageUrl, altText }) => {
  const [isDoubleClicked, setIsDoubleClicked] = useState(false);

  const handleDoubleClick = () => {
    setIsDoubleClicked(!isDoubleClicked);
  };

  if (isDoubleClicked) {
    return <GanttChart />;
  }

  return (
<div>
  <div>
  <img src={imageUrl} alt={altText} onDoubleClick={handleDoubleClick} height={118} width={118} /> </div>
  <div><label>{"Gantt Chart"}</label></div>
</div>
  );
};

export default ThumbnailGantt
