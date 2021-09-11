
import { CREATE_POST,END_LOADING, START_LOADING } from "../actions/types";



export default function (state = { posts: [],isLoading:false }, action) {
    const { type, payload } = action
   
    switch (type) {

        case START_LOADING:
            return { ...state, isLoading: true };
          case END_LOADING:
            return { ...state, isLoading: false };

        case CREATE_POST:
            return { ...state, posts: [payload] };
      

        default:
            return state;
    }
}