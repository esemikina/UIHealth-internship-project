import React, { useState,useEffect } from "react";
import TestButton from "../Components/TestButton";
import styles from "./Home.module.css"

function Home () {
  // set variables [chosen, setChosen] using hooks (useState) to "button 1"
  const [chosen, setChosen] = useState("Button 1")

  // set variables [message, setMessage] using hooks (useState) to "you choose 1"
  const [message, setMessage] = useState("You choose 1")


  useEffect(() =>{
    setMessage(chosen === "Button 1" ? "You choose 1" : "You choose 2" )
  },[chosen])

  // handle currency button onclick
  const changeChosen = (clickedButton) =>{
    setChosen(clickedButton);
  }

  return (
      <div /* exercise 9.2 set classname to first box CSS*/>
        <div /* exercise 9.2 set classname to second box CSS*/>
          <TestButton chosen={chosen} changeChosen={changeChosen}/>
           {/* exercise 9.1 insert TestButton pass chosen and changeChosen ( pass by chosen={chosen})*/}
          {message}
        </div>
      </div>
  );

}

export default Home;
