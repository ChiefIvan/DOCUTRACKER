export type Styles = {
  elementHeight: string;
  elementDisplay: string;
  elementJustify: string;
};

export const elementGet = (styles: Styles) => {
  const { elementHeight, elementDisplay, elementJustify } = styles;
  const element: HTMLElement | null = document.getElementById("app");

  if (!element) {
    console.warn('Element with id "app" not found');
    return () => {};
  }

  element.style.height = elementHeight;
  element.style.display = elementDisplay;
  element.style.justifyContent = elementJustify;

  return () => {
    element.removeAttribute("style");
  };
};
