import React, { useState, useEffect } from 'react';
import World from "@svg-maps/world";
import { SVGMap } from "react-svg-map";
import Styles from "./styles.module.css";

import MapChart from "./MapChart";

export default function App() {
  const [focusedLocation, setFocusedLocation] = useState(null);
  const [randomLocations, setRandomLocations] = useState([]);
  
  const handleLocationFocus = (event) => {
    setFocusedLocation(event.target.id);
  };

  useEffect(() => {
    // Generate random locations
    const generateRandomLocations = (numLocations) => {
      const locations = [];
      for (let i = 0; i < numLocations; i++) {
        const lat = (Math.random() * 180 - 90).toFixed(2); // Latitude between -90 and 90
        const lon = (Math.random() * 360 - 180).toFixed(2); // Longitude between -180 and 180
        locations.push({ id: i, lat, lon });
      }
      return locations;
    };

    setRandomLocations(generateRandomLocations(20)); // Generate 10 random locations
  }, []);

  return (
    <div className={Styles.App}>
      
      <svg className={Styles.SvgMapOverlay}>
        {randomLocations.map((location) => (
          <circle
            key={location.id}
            cx={`${(parseFloat(location.lon) + 180) * (1000 / 360)}`} // Convert lon to x coordinate
            cy={`${(90 - parseFloat(location.lat)) * (500 / 180)}`} // Convert lat to y coordinate
            r="5"
            fill="#32de84"
          />
        ))}
      </svg>
      <SVGMap
        map={World}
        className={Styles.SvgMap}
        onLocationMouseOver={handleLocationFocus}
        locationClassName={(location) =>
          location.id === focusedLocation ? Styles.focused : ""
        }
      />
    </div>
  );
}

