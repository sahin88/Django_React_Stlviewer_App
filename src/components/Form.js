import React, { useState } from "react";
import "../css/form.css";
import { useDispatch } from 'react-redux';
import { createPost } from "../actions/action";

function HomeLeftForm({showImage,setImageShow}) {
    const [image, setImage] = useState('');
    const allowed_extentions=['stl']
   
    const dispatch = useDispatch();



    // Check file extension
    const checkExtention=(file_extension)=>{
        if (allowed_extentions.includes(file_extension)){
            return true; 
        }
        else{
             return false
        }
    }

    // Form submission
    const handleSubmitForm = (event) => {
        event.preventDefault()
        let name_list=image.name.split('.')
        const file_extension=name_list[name_list.length-1].toLowerCase()
        if(checkExtention(file_extension)){
            const data = new FormData(); // creates a new FormData object
            data.append("file", image); // add your file to form data
            dispatch(createPost(data))
        }
        else{
            alert("Allowed extensions 'stl' ")
        }
    };


     // File Selection
    const handleChange = (e) => {         
            setImage(e.target.files[0])
    }
    return (
        <form onSubmit={handleSubmitForm}>
            <div className="form_group">
                <label>Select File:</label>
                <input type="file" onChange={handleChange} />
            </div>
            <div className="form_group">
                <label>Show image</label>
                <input type="checkbox" defaultChecked={showImage}  onChange={()=>setImageShow(!showImage)} />
            </div>

            <div className="form_group">
                <input className="formsubmit_btn" type="submit" />
            </div>
        </form>
    );
}

export default HomeLeftForm;
