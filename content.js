// Function to extract the profile name from the LinkedIn page.
function getProfileName() {
  const nameElement = document.querySelector('.text-heading-xlarge');
  return nameElement ? nameElement.innerText.trim() : 'Name not found';
}


// Function to extract the current job title and company.
function getJobTitleAndCompany() {
  const jobElement = document.querySelector('.text-body-medium.break-words');
  if (jobElement) {
    const text = jobElement.innerText.trim();
    const parts = text.split(' at ');
    if (parts.length === 2) {
      return { title: parts[0].trim(), company: parts[1].trim() };
    }
  }
  return { title: 'Job title not found', company: 'Company not found' };
}

// Function to extract the user's work experience.
function getExperience() {
  const experienceSection = document.getElementById('experience');
  if (!experienceSection) {
    return { experience: 'Experience section not found' };
  }

  const experienceItems = experienceSection.querySelectorAll('.pvs-entity');
  const experiences = [];

  experienceItems.forEach(item => {
    const titleElement = item.querySelector('.t-bold span[aria-hidden="true"]');
    const companyElement = item.querySelector('.t-14.t-normal span[aria-hidden="true"]');
    const dateElement = item.querySelector('.t-14.t-normal.t-black--light span[aria-hidden="true"]');

    if (titleElement && companyElement && dateElement) {
      experiences.push({
        title: titleElement.innerText.trim(),
        company: companyElement.innerText.trim().split(' · ')[0],
        duration: dateElement.innerText.trim()
      });
    }
  });

  return { experience: experiences };
}


// Send the extracted data to the background script.
chrome.runtime.sendMessage({
  profileData: {
    name: getProfileName(),
    ...getJobTitleAndCompany(),
    ...getExperience()
  }
});
