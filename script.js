document.getElementById('submissionForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const formData = new FormData(this);

  fetch('/analyze', {
    method: 'POST',
    body: formData
  })
  .then(res => res.json())
  .then(data => {
    document.querySelector('.result-box').classList.remove('hidden');
    document.getElementById('flagged').textContent = data.flagged ? 'Yes 🚩' : 'No ✅';
    document.getElementById('confidence').textContent = data.confidence;
    document.getElementById('reason').textContent = data.reason;
    document.getElementById('highlight').textContent = `"${data.highlight}"`;
    document.getElementById('suggestion').textContent = data.suggestion;
  });
});
{
  "source";"This is the original project description written by the instructor.",
  "suspicious"; "This is the original project description written by the instructor."
}