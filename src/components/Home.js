import React,{Fragment, useState} from "react";
import "../css/home.css";
import Form from "../components/Form";
import { useSelector} from 'react-redux';
import Spinner from "./Spinner";

 function Home() {

    const {posts, isLoading} = useSelector((state) => state.post);
    const [showImage, setImageShow]= useState(true)
    return (
        <div className="home">
                    {posts.map((client, index) => {
                        return (
                            <Fragment>

                            {isLoading?<Spinner/>:<div key={index + 1} className="home_info_card">
                                <div className="bounding_box">
                                    <h3>Bounding Box</h3>
                                    <div  className="bounding_box_columns">
                                    <p className="bounding_box_column">
                                    <span>Height [mm]:</span> {client.height.toFixed(3)}   
                                    </p>
                                    <p className="bounding_box_column">
                                    <span>Width [mm] : </span> {client.width.toFixed(3)}   
                                    </p>
                                    <p className="bounding_box_column">
                                    <span>Length [mm] : </span> {client.width.toFixed(3)}   
                                    </p>
                                    </div>
                                </div>
                                <div className="bounding_box">
                                    <h3>Volume</h3>
                                    <div  className="bounding_box_columns">
                                    <p className="bounding_box_column">
                                    <span>Volume [mm³]:</span> {client.volume.toFixed(3)}   
                                    </p>
                                   
                                    </div>
                                
                                </div>
                                <div className="bounding_box">
                                    <h3>Surface Area</h3>
                                    <div  className="bounding_box_columns">
                                    <p className="bounding_box_column">
                                    <span>Surface Area [mm²]:</span> {client.total_area.toFixed(3)}   
                                    </p>
                                   
                                    </div>
                                
                                </div>
                            </div>}
                            {showImage?<div className='home_image_card' style={{...style.image_style,backgroundImage:`url("data:image/png;base64, ${client.graph}")`}}></div>:null}
                            </Fragment>
                        );
                    })}
              
                <div className="home_form">
                    <Form  showImage={showImage} setImageShow={setImageShow} />
                </div>
            </div>
    );
}

const style={
    image_style:{
        backgroundImage:'url()',
        border:'1px solid res',
        backgroundPosition:'center',
        backgroundSize:'contain',
        backgroundRepeat:'no-repeat'
    }
}
export default Home;