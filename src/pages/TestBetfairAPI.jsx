import React, { useState } from 'react';
import { Box, Button, Text } from '@chakra-ui/react';

const TestBetfairAPI = () => {
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const testAPIConnection = async () => {
    setLoading(true);
    try {
      const res = await fetch('/api/test-betfair');
      const data = await res.json();
      setResponse(data);
    } catch (error) {
      setResponse({ error: 'Failed to connect to Betfair API' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box p={4}>
      <Button onClick={testAPIConnection} isLoading={loading}>
        Test Betfair API Connection
      </Button>
      {response && (
        <Box mt={4}>
          <Text>{response.error ? response.error : JSON.stringify(response)}</Text>
        </Box>
      )}
    </Box>
  );
};

export default TestBetfairAPI;