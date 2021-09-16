import { CREATE_POST,END_LOADING, START_LOADING } from "./types";
import axios from 'axios';

export const createPost = (newpost) => async (dispatch) => {


        dispatch({type:START_LOADING})
         await axios.post(`http://localhost:8000/post`, newpost, {
         
        }).then(res=>{
            dispatch({ type: CREATE_POST, payload: res.data })
        }).catch(err=>{
            alert("error from backend"+err.response.data.detail)
        })
        
        dispatch({ type: END_LOADING });

    

}
