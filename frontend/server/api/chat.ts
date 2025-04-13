export default defineEventHandler(async (event) => {

  const url = "http://localhost:8000/chat";


  const response = await fetch(url, {
    method: 'GET',
  });

  if (!response.ok) {
    throw createError({ statusCode: response.status, message: "Failed to fetch data" });
  }

  event.node.res.setHeader('Content-Type', 'text/plain');
  event.node.res.setHeader('Transfer-Encoding', 'chunked');

  console.log("Returning the response stream");

  const stream = response.body;

  if (stream) {
    return sendStream(event, new ReadableStream(stream))
  }
});
