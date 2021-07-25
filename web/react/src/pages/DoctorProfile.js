import React, { useEffect, useState } from "react";
import "../assets/css/doctor-profile.css";
import doctorsData from "../dummy-data";

const DoctorProfile = (props) => {
  const [data, setData] = useState({});

  //   const search = useLocation().search;
  //   const id = new URLSearchParams(search).get('id');
  let { id } = props.match.params;
  id = parseInt(id);

  useEffect(() => {
    console.log(doctorsData);
    const res = doctorsData.filter((item) => item.id === id);
    console.log(res);
    setData(res[0]);
  },[id]);

  return (
    <div className="doctor-profile" style={{ marginTop: "3rem" }}>
      <div className="jumbotron">
        <div className="d-flex flex-column justify-content-center align-items-center p-5">
          <img className="doctor-img mb-3" src={data.image} alt="" />
          <h2>{data.name}</h2>
          <h3>{data.post}</h3>
          <div className="mt-3">
          <a className=" button mr-3" href="http://localhost/bright.ai/videoCall.html">
           Video Consultation
          </a>

          <a className=" button" href="http://localhost/bright.ai/chatting/index.php">
          Chatting
          </a>
          </div>
        </div>
      </div>

      <div className="container">
        <div className="about-section">
          <h2 className="subheading text-center">About</h2>
          <p>{data.about}</p>
        </div>
      </div>
    </div>
  );
};

export default DoctorProfile;
