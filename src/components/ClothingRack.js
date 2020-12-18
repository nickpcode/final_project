import React, { Component } from "react";

export default class ClothingRack extends Component {
  constructor(props) {
    super(props);
    this.state = {
      shirt: "https://i.imgur.com/6Lgf8aG.jpg",
      jacket: "https://i.imgur.com/Xf0MV0v.jpg",
      pant: "https://i.imgur.com/Yq7aeCT.jpg",
      shoe: "https://i.imgur.com/KfyM2je.jpg",
    };
  }

  showShirt(shirt) {
    this.setState({});
  }

  render() {
    return (
      <div>
        <img src={this.state.shirt} />
        <img src={this.state.jacket} />
        <br />
        <img src={this.state.pant} />
        <br />
        <img src={this.state.shoe} />
      </div>
    );
  }
}
