import redis, { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();
client.get = promisify(client.get);

client.on('error', err => {
  console.log('Redis client not connected to the server: ', err);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
  const reply = await client.get(schoolName);
  console.log(reply);
};


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
