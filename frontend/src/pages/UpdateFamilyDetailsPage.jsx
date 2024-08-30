import React, { useCallback, useEffect, useRef, useState } from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import AddIcon from "@mui/icons-material/Add";
import Button from "@mui/material/Button";
import api from "../api";
import { Navigate, useNavigate } from "react-router-dom";

const UpdateFamilyDetailsPage = () => {
  const [brothers, setBrothers] = useState([{ name: "" }]);
  const [sisters, setSisters] = useState([{ name: "" }]);
  const [fatherName, setFatherName] = useState("");
  const [motherName, setMotherName] = useState("");
  const [grandFatherName, setGrandFatherName] = useState("");
  const [grandMotherName, setGrandMotherName] = useState("");
  const [totalFamilyMembers, setTotalFamilyMembers] = useState("");
  const familyDetailsId = useRef()
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate()

  const addBrotherField = useCallback(() => {
    setBrothers((prevBrothers) => [...prevBrothers, { name: "" }]);
  }, []);

  const addSisterField = useCallback(() => {
    setSisters((prevSisters) => [...prevSisters, { name: "" }]);
  }, []);

  const handleBrotherChange = useCallback((index, event) => {
    const { value } = event.target;
    setBrothers((prevBrothers) => {
      const newBrothers = [...prevBrothers];
      newBrothers[index].name = value;
      return newBrothers;
    });
  }, []);

  const handleSisterChange = useCallback((index, event) => {
    const { value } = event.target;
    setSisters((prevSisters) => {
      const newSisters = [...prevSisters];
      newSisters[index].name = value;
      return newSisters;
    });
  }, []);

  
  const getFamilyDetails = async () => {
    setLoading(true);
    try {
      const res = await api.get("/api/user/family-details/");
      if (res.data.length > 0) {
        setSisters(res.data[0].sisters);
        setBrothers(res.data[0].brothers);
        setFatherName(res.data[0].father_name);
        setMotherName(res.data[0].mother_name);
        setTotalFamilyMembers(res.data[0].total_members);
        setGrandFatherName(res.data[0].grandfather_name);
        setGrandMotherName(res.data[0].grandmother_name);
        familyDetailsId.current = res.data[0].id
      }
    } catch (error) {
      alert(error);
    } finally {
      setLoading(false);
    }
  };
  useEffect(() => {
    getFamilyDetails();
  }, []);

  const handleFormSubmit = async (e) => {
    e.preventDefault();
    console.log(
      totalFamilyMembers,
      fatherName,
      motherName,
      grandFatherName,
      grandMotherName,
      brothers,
      sisters,
      "details"
    );
    setLoading(true);
    try {
      const res = await api.put(`/api/user/family-details/${familyDetailsId.current}/`, {
        total_members: totalFamilyMembers,
        father_name: fatherName,
        mother_name: motherName,
        grandfather_name: grandFatherName,
        grandmother_name: grandMotherName,
        brothers,
        sisters,
      });
      if (res.status == 200) {
        console.log("family details updated successfully")
        navigate("/");
      } else {
        alert("Error while adding family details");
      }
    } catch (error) {
      alert(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <form onSubmit={handleFormSubmit}>
        <Box
          sx={{
            //   display: "flex",
            //   flexDirection: "column",
            //   alignItems: "center",
            //   justifyContent: "center",
            //   borderRadius: "8px",
            //   boxShadow: "0 4px 6px rgba(0, 0, 0, 0.1)",
            margin: "25px auto",
            padding: "20px",
          }}
        >
          <div>
            <h3>Update Family Details</h3>
          </div>
          <TextField
            id="demo-helper-text-misaligned-no-helper"
            style={{ paddingTop: "4px" }}
            label="Total Family Members"
            value={totalFamilyMembers}
            onChange={(e) => setTotalFamilyMembers(e.target.value)}
            fullWidth
          />
          <TextField
            id="demo-helper-text-misaligned-no-helper"
            style={{ paddingTop: "4px" }}
            label="Father Name"
            value={fatherName}
            onChange={(e) => setFatherName(e.target.value)}
            fullWidth
          />
          <TextField
            id="demo-helper-text-misaligned-no-helper"
            style={{ paddingTop: "4px" }}
            label="Mother Name"
            value={motherName}
            onChange={(e) => setMotherName(e.target.value)}
            fullWidth
          />
          <TextField
            id="demo-helper-text-misaligned-no-helper"
            style={{ paddingTop: "4px" }}
            label="Grand Father Name"
            value={grandFatherName}
            onChange={(e) => setGrandFatherName(e.target.value)}
            fullWidth
          />
          <TextField
            id="demo-helper-text-misaligned-no-helper"
            style={{ paddingTop: "4px" }}
            label="Grand MotherName"
            value={grandMotherName}
            onChange={(e) => setGrandMotherName(e.target.value)}
            fullWidth
          />

          <div
            style={{
              paddingTop: "4px",
              display: "flex",
              width: "100%",
              flexDirection: "column",
              gap: "6px",
            }}
          >
            {brothers.map((brother, index) => (
              <TextField
                key={index}
                id={`brother-name-${index}`}
                label="Brother Name"
                fullWidth
                value={brother.name}
                onChange={(event) => handleBrotherChange(index, event)}
                style={{ paddingTop: "4px" }}
              />
            ))}
            <Button
              variant="outlined"
              style={{ height: "100%" }}
              onClick={addBrotherField}
            >
              <AddIcon />
            </Button>
          </div>

          <div
            style={{
              paddingTop: "4px",
              display: "flex",
              width: "100%",
              flexDirection: "column",
              gap: "6px",
            }}
          >
            {sisters.map((sister, index) => (
              <TextField
                key={index}
                id={`sister-name-${index}`}
                label="Sister Name"
                fullWidth
                value={sister.name}
                onChange={(event) => handleSisterChange(index, event)}
                style={{ paddingTop: "4px" }}
              />
            ))}
            <Button
              variant="outlined"
              style={{ height: "100%" }}
              onClick={addSisterField}
            >
              <AddIcon />
            </Button>
          </div>

          <div
            style={{
              paddingTop: "4px",
              marginTop: "20px",
              width: "100%",
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            <Button
              variant="outlined"
              style={{ height: "100%", padding: "15px" }}
              type="submit"
            >
              Update Family Details
            </Button>
          </div>
        </Box>
      </form>
    </div>
  );
};

export default UpdateFamilyDetailsPage;
