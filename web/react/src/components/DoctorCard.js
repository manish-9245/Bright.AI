import React from 'react';
import { Link } from "react-router-dom";
import "../assets/css/doctor-card.css"

const DoctorCard = ({doctor}) => {
    const url = `/doctor/${doctor.id}`

    return (
        <div className="doctor-card">
        <img src={doctor.image} className="doctor-img" alt="" />
        <h3>{ doctor.name}</h3>
        <h4> {doctor.post} </h4>
        {/* <p>
          <i className="bx bxs-quote-alt-left quote-icon-left"></i>
          Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam, risus at semper.
          <i className="bx bxs-quote-alt-right quote-icon-right"></i>
        </p> */}

        <div className="doctor-details d-flex">
            <div className=" doctor-details-item d-flex flex-column justify-content-around align-items-center ">
            <h4>Location</h4>
             <p>{doctor.location}</p>
            </div>
            <div className="doctor-details-item d-flex flex-column justify-content-around align-items-center">
            <h4>Qualification</h4>
            <p>{doctor.qualification}</p>
            </div>
            <div className="doctor-details-item d-flex flex-column justify-content-around align-items-center">
            <h4>Specialization</h4>
            <p>{doctor.specialization[0]}</p>
            </div>
        </div>

        <div className="doctor-card-footer text-end mt-3">
        <Link className="button " to={url} >View Profile</Link>
        </div>
      </div>
    )
}

export default DoctorCard;


			