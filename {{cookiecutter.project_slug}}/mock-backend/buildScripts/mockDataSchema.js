var api = {
  "type": "object",
  "properties": {
    "users": {
      "type": "array",
      "minItems": 5,
      "maxItems": 10,
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "number",
            "unique": true,
            "minimum": 1
          },
          "firstName": {
            "type": "string",
            "faker": "name.firstName"
          },
          "lastName": {
            "type": "string",
            "faker": "name.lastName"
          },
          "email": {
            "type": "string",
            "faker": "internet.email"
          }
        },
        "required": ["id", "type", "lastname", "email"]
      }
    },
    "products": {
      "type": "array",
      "minItems": 10,
      "maxItems": 15,
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "number",
            "unique": true,
            "minimum": 1
          },
          "name": {
            "type": "string",
            "faker": "commerce.productName"
          },
          "price": {
            "type": "string",
            "faker": "commerce.price"
          },
          "color": {
            "type": "string",
            "faker": "commerce.color"
          },
          "brand": {
            "type": "string",
            "faker": "company.companyName"
          }
          
        },
        "required": ["id", "name", "brand", "price", "color"]
      }
    }
  },
  "required": ["users", "products"]
};

module.exports = api
