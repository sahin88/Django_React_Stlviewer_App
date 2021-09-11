import { CREATE_POST,END_LOADING, START_LOADING } from "./types";
import axios from 'axios';

export const createPost = (newpost) => async (dispatch) => {

    try {
        dispatch({type:START_LOADING})
        const { data } = await axios.post(`http://localhost:8000/post`, newpost, {
          
        })

        dispatch({ type: CREATE_POST, payload: data })
        dispatch({ type: END_LOADING });
        return data

    } catch (error) {

        alert("Error from backend", error)
    }
}


