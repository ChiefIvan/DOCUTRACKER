<footer>
  <div>Copyright 2023 DOCUTRACKER</div>
</footer>

<style>
  footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    padding: 0.5rem;
    text-align: center;

    & div {
      color: #aaa;
      font-size: 0.9rem;
      display: inline-block;
      padding: 1rem;
      border-top: 1px solid #ddd;
    }
  }

  @media (max-height: 600px) {
    footer {
      position: static;
    }
  }
</style>
