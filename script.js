function loadContent(section) {
    fetch(`${section}.json`)
        .then(response => response.json())
        .then(data => {
            let content = `<h2>${section.charAt(0).toUpperCase() + section.slice(1)}</h2>`;
            content += generateList(data);
            document.getElementById('content').innerHTML = content;
        })
        .catch(error => console.error('Error:', error));
}

function generateList(data, path = '') {
    let list = '<ul>';
    for (let key in data) {
        if (typeof data[key] === 'object') {
            list += `<li>${key}/`;
            list += generateList(data[key], path + key + '/');
            list += '</li>';
        } else {
            list += `<li><a href="${path}${data[key]}">${key}</a></li>`;
        }
    }
    list += '</ul>';
    return list;
}