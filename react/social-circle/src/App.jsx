import React, { useEffect, useState } from "react";
import Create from "./components/create_user";

const App = () =>{
  const [message,setMessage]=useState("");
  const getWelcomeMessage= async() =>{
    const requestOptions ={
      method: "GET",
      headers:{
        "Content-Type":"application/json",

      },
    };
    const response=await fetch("http://localhost:8000/api",requestOptions);
    const data=await response.json();
    if (!response.ok){
      console.log("something messed up");
      } else {
        setMessage(data.message);

    }


  };

  useEffect(() =>{
    getWelcomeMessage();
  },[])
  return(
    <div>
      <h1>
       {message}
      </h1>
      <Create />

      
    </div>

  );
};

export default App
