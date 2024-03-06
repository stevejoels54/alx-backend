import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const client = createClient();
const port = 1245;

const clientGet = promisify(client.get).bind(client);
const clientSet = promisify(client.set).bind(client);

const reserveSeat = async (number) =>  await clientSet('available_seats', number);
const getCurrentAvailableSeats = async () => await clientGet('available_seats');

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

app.get('/available_seats', async (req, res) => {
    const seats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats: seats });
});

app.get('/reserve_seat', async (req, res) => {
    await reserveSeat(50);
    res.json({ status: 'Reservation confirmed' });
});

app.get('/process', async (req, res) => {
    await reserveSeat(50);
    res.json({ status: 'Reservation confirmed' });
});

app.listen(port, () => {
    console.log(`app listening at http://localhost:${port}`);
});
