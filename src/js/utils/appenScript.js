export const appendScript = (scriptToAppend) => {
    const script = document.createElement("script");

    script.src = "hantor_page/web/js" + scriptToAppend;
    script.async = true;
    document.body.appendChild(script);
}