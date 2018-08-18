import React, { Component } from 'react';
import ProductList from './components/ProductList';

import logo from './logo.svg';
import './App.css';

const API = 'http://localhost:8001';
const DEFAULT_QUERY = '/products';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedProducts: [],
      products: []
    }
  }

  componentWillMount() {
    fetch(API + DEFAULT_QUERY)
      .then(response => response.json())
      .then(data => this.setState({ products: data }));
  }

  handleProductSelect (product) {
    this.setState(prevState => {
      return {
        selectedProducts: prevState.selectedProducts.concat(product)
      }
    });
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1>My Product Store</h1>
        </header>
        <ProductList
          products={this.state.products}
          onProductSelect={this.handleProductSelect.bind(this)}
        />
      </div>
    );
  }
}

export default App;
