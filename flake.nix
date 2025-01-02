{
  description = "Nix flake for capitolscraper";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-24.11";
    nixpkgs-unstable.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = {
    nixpkgs,
    nixpkgs-unstable,
    ...
  }: let
    system = "x86_64-linux";
    pkgs = import nixpkgs {
      inherit system;
      overlays = [
        (final: prev: {
          unstable = import nixpkgs-unstable {
            system = prev.system;
          };
        })
      ];
    };
  in {
    devShells.${system}.default = pkgs.mkShell {

      packages = with pkgs; [
        unstable.uv
        (pkgs.python3.withPackages(ps: [ pkgs.python312Packages.httpx ] ++ pkgs.python312Packages.httpx.optional-dependencies.cli ))
      ];
    };
  };
}
