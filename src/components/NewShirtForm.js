import React, { Component } from "react";

const baseURL = "http://localhost:8000";

export default class NewShirtForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      color: "",
      fabric: "",
      brand: "",
      image: "",
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ [event.target.id]: event.target.value });
  }

  handleSubmit(event) {
    event.preventDefault();
    fetch(baseURL + "/api/v1/shirts/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Allow-Methods": "POST",
      },
      withCredentials: true,
      body: JSON.stringify({
        color: this.state.color,
        fabric: this.state.fabric,
        brand: this.state.brand,
        image: this.state.image,
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        this.props.handleAddShirt(data);
        this.setState({
          color: "",
          fabric: "",
          brand: "",
          image: "",
        });
      });
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <label htmlFor="color">Color</label>
          <input
            type="text"
            id="color"
            name="color"
            onChange={this.handleChange}
            value={this.state.color}
            placeholder="color"
          />
          <br />
          <label htmlFor="fabric">Fabric</label>
          <input
            type="text"
            id="fabric"
            name="fabric"
            onChange={this.handleChange}
            value={this.state.fabric}
            placeholder="fabric"
          />
          <br />
          <label htmlFor="brand">Brand</label>
          <input
            type="text"
            id="brand"
            name="brand"
            onChange={this.handleChange}
            value={this.state.brand}
            placeholder="brand"
          />
          <br />
          <label htmlFor="image">Image</label>
          <input
            type="text"
            id="image"
            name="image"
            onChange={this.handleChange}
            value={this.state.image}
            placeholder="image url"
          />
          <br />
          <input type="submit" value="Add Shirt" />
        </form>
      </div>
    );
  }
}
