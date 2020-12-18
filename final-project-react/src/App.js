import React, { Component } from "react";
import "./index.css";
import "bootstrap/dist/css/bootstrap.min.css";
import ClothingRack from "./components/ClothingRack";
import Shirt from "./components/Shirt";
import Jacket from "./components/Jacket";
import Pant from "./components/Pant.js";
import Shoe from "./components/Shoe.js";

export default class App extends Component {
  componentDidMount() {
    document.body.style.backgroundColor = "rgb(255, 228, 232)";
  }

  render() {
    return (
      <div>
        <h1 class="font-face">Lets Make an Outfit</h1>
        <ClothingRack />
        <Shirt />
        <Jacket />
        <Pant />
        <Shoe />
      </div>
    );
  }
}
