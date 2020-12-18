import React, { Component } from "react";
import { BrowserRouter, Link, Route, Switch } from "react-router-dom";
import "./index.css";
import "bootstrap/dist/css/bootstrap.min.css";
import ClothingRack from "./components/ClothingRack";
import Shirt from "./components/Shirt";
import Jacket from "./components/Jacket";
import Pant from "./components/Pant.js";
import Shoe from "./components/Shoe.js";
import NewShirtForm from "./components/NewShirtForm.js";

export default class App extends Component {
  componentDidMount() {
    document.body.style.backgroundColor = "rgb(255, 228, 232)";
  }

  render() {
    return (
      <BrowserRouter>
        <h1 className="font-face">Lets Make an Outfit</h1>
        <ClothingRack />
        <Shirt />
        <Link to="/newshirt">Add Shirt to Closet</Link>
        <Jacket />
        <Link to="/newjacket">Add Jacket to Closet</Link>
        <Pant />
        <Link to="/newpants">Add Pants to Closet</Link>
        <Shoe />
        <Link to="/newshoe">Add Shoe to Closet</Link>

        <Switch>
          <Route exact path="/newshirt" component={NewShirtForm} />
        </Switch>
      </BrowserRouter>
    );
  }
}
