<script lang="ts">
  export let disabled = true;
  export let checkboxName = "";
  export let checked = false;
</script>

<div class:container-disabled={disabled}>
  <div class="checkbox-wrapper">
    <span>
      <input
        class:disabled
        id="remember"
        type="checkbox"
        {checked}
        class:got-checked={checked}
        {disabled}
        on:change
      />
      <svg class:got-checked={checked}>
        <use xlink:href="#checkbox-30" class="checkbox" />
      </svg>
    </span>
    <svg
      class:got-checked={checked}
      xmlns="http://www.w3.org/2000/svg"
      style="display: none"
    >
      <symbol id="checkbox-30" viewBox="0 0 22 22">
        <path
          fill="none"
          stroke="blue"
          d="M5.5,11.3L9,14.8L20.2,3.3l0,0c-0.5-1-1.5-1.8-2.7-1.8h-13c-1.7,0-3,1.3-3,3v13c0,1.7,1.3,3,3,3h13 c1.7,0,3-1.3,3-3v-13c0-0.4-0.1-0.8-0.3-1.2"
        />
      </symbol>
    </svg>
  </div>
  <label class:disabled for="remember">{checkboxName}</label>
</div>

<style>
  div {
    display: flex;
    column-gap: 0.5rem;

    & label {
      cursor: pointer;
      transition: all 250ms ease-in-out;
      color: var(--main-col-1);
    }

    & label.disabled {
      pointer-events: none;
    }

    & .checkbox-wrapper {
      & span {
        display: inline-block;
        min-width: calc(var(--size, 1) * 20px);
        position: relative;

        & svg {
          fill: none;
          left: 0;
          pointer-events: none;
          stroke: var(--stroke, var(--border-active));
          stroke-dasharray: var(--dashArray, 93);
          stroke-dashoffset: var(--dashOffset, 94);
          stroke-linecap: round;
          stroke-linejoin: round;
          stroke-width: 2px;
          top: 0;
          transition: stroke-dasharray 500ms, stroke-dashoffset 500ms;
        }

        & svg,
        input {
          display: block;
          height: 100%;
          width: 100%;
        }
      }

      & span:after {
        content: "";
        width: 100%;
        padding-top: 100%;
        display: block;
      }

      & input {
        -webkit-appearance: none;
        -moz-appearance: none;
        -webkit-tap-highlight-color: transparent;
        cursor: pointer;
        background-color: var(--background);
        border-radius: calc(var(--size, 1) * 4px);
        border: calc(var(--newBrdr, var(--size, 1)) * 1px) solid;
        color: var(--border-color);
        outline: none;
        margin: 0;
        padding: 0;
        transition: all 250ms linear;
      }

      & input.disabled {
        pointer-events: none;
      }

      & input.got-checked {
        color: var(--newBrdrClr);
      }

      & input:hover,
      input:checked {
        --newBrdr: var(--size, 1);
      }

      & input:checked {
        --newBrdrClr: var(--border-active-color);
        transition-delay: 200ms;
      }
    }

    & .checkbox-wrapper span > * {
      position: absolute;
    }

    & .checkbox-wrapper span input:checked + svg.got-checked {
      --dashArray: 16 93;
      --dashOffset: 109;
    }
  }

  div.container-disabled {
    cursor: not-allowed;
  }

  div:hover label {
    color: var(--scroll-color);
  }

  div.container-disabled:hover input {
    cursor: not-allowed;
  }

  div.container-disabled:hover label {
    cursor: not-allowed;
    color: var(--main-col-1);
  }
</style>
