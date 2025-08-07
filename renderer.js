const { exec } = require('child_process');

function organizeFiles() {
  const folder = document.getElementById('folderPath').value;
  document.getElementById('status').innerText = 'Organizing...';

  exec(`python organizer.py "${folder}"`, (error, stdout, stderr) => {
    if (error) {
      document.getElementById('status').innerText = `Error: ${stderr}`;
      return;
    }
    document.getElementById('status').innerText = stdout;
  });
}
