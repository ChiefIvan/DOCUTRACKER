<script>
  export let btnName = "";
  export let btnLoginSize = false;
  export let btnSignupSize = false;
  export let btnDisabled = false;
  export let btnTitle = "";
</script>

<button
  class:change-login-size={btnLoginSize}
  class:change-signup-size={btnSignupSize}
  class:btn-disabled={btnDisabled}
  title={btnDisabled && btnTitle}
  disabled={btnDisabled}
>
  {btnName}
</button>

<style>
  button {
    height: 2rem;
    border: none;
    color: white;
    background-color: orange;
    cursor: pointer;
    border-radius: 5px;
    transition: all ease-in-out 300ms;
  }

  button.change-login-size {
    width: 100%;
  }

  button.change-signup-size {
    width: 8rem;
  }

  button:hover {
    opacity: var(--opacity);
    box-shadow: 5px 5px 25px gray;
  }

  button.btn-disabled {
    background-color: gray;
    box-shadow: none;
    opacity: 1;
    cursor: not-allowed;
  }
</style>
