import tippy, { type TippyProps } from "svelte-tippy";
import "tippy.js/dist/tippy.css";
import "tippy.js/animations/perspective-subtle.css";

type Options = Partial<TippyProps>;

export const tooltip = (element: HTMLElement, options: Options) => {
  const tooltip = tippy(element, options);

  return {
    destroy() {
      tooltip.destroy();
    },
  };
};
