import React, { useEffect, useState } from "react";

const Create = () =>
    {
        const [email_id,setEmail_id]=useState("");
        const [password,setPassword]=useState("");

        const SubmitCreate = async () => {
            const requestOptions={
                method:"POST",
                headers: {"Content-Type":"application/json"},
                body:JSON.stringify({email_id: email_id,password: password}), 
            };
            const response=await fetch("http://localhost:8000/user/",requestOptions);
            const data=await response.json();
            console.log(data)
        
        };

            const handleSubmit= (e) =>{
                e.preventDefault();
                SubmitCreate();
                
            }
        return(
            <div className="column" onSubmit={handleSubmit}>
                <form  className="box" >
                    <h1 className="title has-text-centered">Create User</h1>
                    <div className="field">
                        <label  className="label">email_id</label>
                        <div className="control">
                            <input type="email" placeholder="enter email_id" value={email_id} onChange={(e) => setEmail_id(e.target.value)} className="input" />
                        </div>
                    </div>

                    <div className="field">
                        <label  className="label">Password</label>
                        <div className="control">
                            <input type="password" placeholder="enter password" value={password} onChange={(e) => setPassword(e.target.value)} className="input" />
                        </div>
                    </div>
                    <button className="button is-primary" type="submit">
                        Create
                    </button>
                </form>
            </div>
        );
    };

export default Create;

