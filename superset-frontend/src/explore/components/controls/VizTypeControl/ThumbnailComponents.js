import React from 'react';
// image = "https://www.smartsheet.com/sites/default/files/styles/1300px/public/2021-05/IC-Gantt-Chart-Example-Product-Development_WORD.png?itok=kST_-09R"

// Component 1
export function WaterfallThumbnail() {
  return (
  <div>
    <div>
    <img src={"https://datavizcatalogue.com/methods/images/top_images/bubble_chart.png"} alt={altText} height={118} width={118} /> 
    </div>
    <div><label>{"Waterfall Chart"}</label></div>
  </div>);
}

// Component 2
export function BubbleThumbnail() {
    return (
    <div>
      <div>
      <img src={"https://datavizcatalogue.com/methods/images/top_images/bubble_chart.png"} alt={"Bubble Chart"} height={118} width={118} /> 
      </div>
      <div><label>{"Bubble Chart"}</label></div>
    </div>);
  }
// export {BubbleThumbnail};

// Component 3
export function HistogramThumbnail() {
    return (
    <div>
      <div>
      <img src={"https://images.squarespace-cdn.com/content/v1/55b6a6dce4b089e11621d3ed/1611887632387-L44QASP3HYOAK2NPV8YZ/Histogram+example.jpg"} alt={"Histogram"} height={118} width={118} /> 
      </div>
      <div><label>{"Histogram"}</label></div>
    </div>);
  }
// export {HistogramThumbnail};

// Component 4
export function HeatmapThumbnail() {
    return (
    <div>
      <div>
      <img src={"https://static.anychart.com/images/gallery/v8/heat-map-charts-heat-map-with-scroll.png"} alt={"HeatMap"} height={118} width={118} />
       </div>
      <div><label>{"HeatMap"}</label></div>
    </div>);
  }
// export {HeatmapThumbnail};

// Component 5
export function RadarThumbnail() {
    return (
    <div>
      <div>
      <img src={"https://images.edrawmax.com/images/knowledge/radar-chart-2-element.jpg"} alt={"Radar Chart"} height={118} width={118} /> 
      </div>
      <div><label>{"Radar Chart"}</label></div>
    </div>);
  }
// export {RadarThumbnail};