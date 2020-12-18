import React, { Component } from "react";

const baseURL = "http://localhost:8000";

export default class Shirt extends Component {
  constructor(props) {
    super(props);
    this.state = {
      shirts: [
        {
          shirt: {
            color: "",
            fabric: "",
            brand: "",
            image: "",
          },
        },
      ],
    };
    this.getShirts = this.getShirts.bind(this);
    this.handleAddShirt = this.handleAddShirt.bind(this);
  }

  handleAddShirt(shirt) {
    this.setState({
      shirts: this.state.shirts.concat(shirt),
    });
  }

  getShirts() {
    fetch(baseURL + "/api/v1/shirts/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Allow-Methods": "GET",
      },
    })
      .then((data) => {
        // console.log(data);
        return data.json();
      })
      .then((parsedData) => {
        // console.log(parsedData);
        this.setState({
          color: parsedData,
          fabric: parsedData,
          brand: parsedData,
          image: parsedData,
        });
      });
  }

  donateShirt(id) {
    fetch(baseURL + "/api/v1/shirts/" + id, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Allow-Methods": "DELETE",
      },
      withCredentials: true,
    }).then((response) => {
      const findIndex = this.state.findIndex((shirt) => shirt._id === id);
      const copyShirts = [...this.state.shirts];
      copyShirts.splice(findIndex, 1);
      this.setState({ shirts: copyShirts });
    });
  }

  render() {
    return (
      <tr key={this.props.id}>
        <td>{this.state.shirts.color}</td>
        <td>{this.state.shirts.fabric}</td>
        <td>{this.state.shirts.brand}</td>
        <td onClick={() => this.props.donateShirt(this.props.shirt._id)}>X</td>
        {/* <td>
            <button onClick={() => this.props.editDog(this.props.dog._id)}>
              Edit Dog
            </button>
          </td> */}
      </tr>
    );
  }
}

// https://i.imgur.com/6Lgf8aG.jpg

// https://i.imgur.com/HcXhlPa.jpg
