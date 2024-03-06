import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const client = createClient();
const port = 1245;

const getAsync = promisify(client.get).bind(client);

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

const listProducts = [
    { itemId: 1, itemName: 'Suitcase 250', price: 50, stock: 4 },
    { itemId: 2, itemName: 'Suitcase 450', price: 100, stock: 10 },
    { itemId: 3, itemName: 'Suitcase 650', price: 350, stock: 2 },
    { itemId: 4, itemName: 'Suitcase 1050', price: 550, stock: 5 }
];

function getItemById(id) {
    const item = listProducts.find((item) => item.itemId === id);
    return item;
}

app.get('/list_products', (req, res) => {
    res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
    const itemId = req.params.itemId;
    const item = getItemById(parseInt(itemId));

    if (!item) {
        res.json({ status: 'Product not found' });
        return;
    }

    const stock = await getAsync(`item_${itemId}`);
    if (stock) {
        item.currentQuantity = stock;
    }
    res.json(item);
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = req.params.itemId;
    const item = getItemById(parseInt(itemId));

    if (!item) {
        res.json({ status: 'Product not found' });
        return;
    }

    const stock = await getAsync(`item_${itemId}`);
    if (stock > 0) {
        client.set(`item_${itemId}`, stock - 1);
        res.json({ status: 'Reservation confirmed', itemId: itemId });
    } else {
        res.json({ status: 'Not enough stock available', itemId: itemId });
    }
});

app.listen(port, () => {
    console.log(`app listening at http://localhost:${port}`);
});
