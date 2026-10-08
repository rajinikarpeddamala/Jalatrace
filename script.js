function showMessage() {

    alert(
        "JalaTrace Dashboard will be available soon!"
    );

}


function scrollToSection(sectionId) {

    const section =
        document.getElementById(sectionId);

    section.scrollIntoView({
        behavior: "smooth"
    });

}