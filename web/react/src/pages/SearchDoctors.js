import React from "react";
import DoctorCard from "../components/DoctorCard";
import "../assets/css/search.css";
import doctorsData from "../dummy-data";

const SearchDoctors = () => {
  return (
    <div style={{ marginTop: "3rem" }}>
      <div className="search-doctors">
        <div className="search-doctors">
          <div className =" row justify-content-center">
            <div className="col-lg-6">
              <h4>Search Doctors</h4>
              <p>Enter location to get nearby doctors</p>
              <form action="" method="post">
                <input type="text" name="location" />
                <input type="submit" value="Search" />
              </form>
            </div>
          </div>
        </div>
      </div>
      <div className=" container ">
          <div className="doctors-list">
              {doctorsData.map(item => { 
                  return  <DoctorCard doctor={item} key={item.id} />
            })}
      </div>
      </div>
    </div>
  );
};

export default SearchDoctors;
