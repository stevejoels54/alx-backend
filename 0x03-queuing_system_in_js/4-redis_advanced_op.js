import redis from 'redis';
import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

const name = 'HolbertonSchools';
const values = { Portland: 50, Seattle: 80, 'New York': 20, Bogota: 20, Cali: 40, Paris: 2 };

for (const key in values) {
    client.hset(name, key, values[key], (_, reply) => {
        redis.print(`Reply: ${reply}`);
    });
}

client.hgetall(name, (_, object) => {
    console.log(object);
});
