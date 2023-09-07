<script>
  import { afterUpdate } from "svelte";
  import { entryState, resetInput } from "../../stores";

  export let inputName = "";
  export let inputType = "";
  export let inputAutocomplete = "";
  export let inputValue = "";

  let activeFocus = false;
  let inputState = false;

  afterUpdate(() => {
    if ($entryState) {
      if (inputValue.length === 0) {
        inputState = false;
        // return;
      }
    }
  });

  const handleOnfocus = (e) => {
    inputState = true;
    activeFocus = true;
    $entryState = false;
  };

  const handleOfffocus = (event) => {
    activeFocus = false;

    if (event.target.value) {
      return;
    }

    inputState = false;
  };
</script>

<div>
  <label
    class:active-slide={inputState}
    class:focus-active={activeFocus}
    for={inputName}>{inputName}</label
  >
  <input
    required
    title={inputType === "password"
      ? "Your password must atleast 7 characters long!"
      : "Please fiil out this field"}
    id={inputName}
    class:focus-active={activeFocus}
    type={inputType}
    autocomplete={inputAutocomplete}
    value={inputValue}
    bind:this={$resetInput}
    on:focus={handleOnfocus}
    on:blur={handleOfffocus}
    on:input
  />
</div>

<style>
  :root {
    --transition: all ease-in-out;
    --entry-color: lightgray;
    --contrastcolor: blue;
  }

  div {
    display: flex;
    align-items: center;
    position: relative;
  }

  label {
    font-size: 1.2rem;
    user-select: none;
    transition: var(--transition) 250ms;
    padding: 1.1rem;
    color: gray;
    cursor: text;

    position: absolute;
    z-index: -1;
  }

  label.active-slide {
    font-size: 0.7rem;
    padding: 0 1rem;
    transform: translateY(-1.4rem);
  }

  label.focus-active {
    color: var(--contrastcolor);
  }

  input {
    height: 2rem;
    width: 25rem;
    padding: 0 1rem;
    transition: var(--transition) 300ms;
    border: 1px solid transparent;
    border-bottom: 1px solid var(--entry-color);
    outline: none;
    background: transparent;
  }

  div:hover input {
    border-bottom: 1px solid orange;
  }

  div:hover label {
    color: orange;
  }

  input.focus-active {
    border-bottom: 1px solid var(--contrastcolor);
  }
</style>
