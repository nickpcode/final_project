import React, { Component } from "react";

const baseURL = "http://localhost:8000";

export default class Shirt extends Component {
  constructor(props) {
    super(props);
    this.state = {
      shirts: [],
    };
    this.getShirts = this.getShirts.bind(this);
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
          name: parsedData,
        });
      });
  }

  render() {
    return <div></div>;
  }
}

// https://i.imgur.com/6Lgf8aG.jpg
