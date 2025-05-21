const express = require("express");
const { MongoClient } = require("mongodb");
const dotenv = require("dotenv");
const path = require("path");

// Load .env from root directory
dotenv.config();

const app = express();
const port = 3000;
const uri = process.env.mongo_uri;

app.get("/api/products", async (req, res) => {
  let client;
  try {
    client = await MongoClient.connect(uri);
    const db = client.db("testdb");
    const products = await db
      .collection("products")
      .find({}, { projection: { _id: 0 } })
      .toArray();
    res.json(products);
  } catch (err) {
    res.status(500).json({ error: err.message });
  } finally {
    if (client) await client.close();
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
