{

	inputs = {


		nixpkgs = {
			url = "github:nixos/nixpkgs/nixos-unstable";

		};
		flake-utils = {
			url = "github:numtide/flake-utils";
		};

	};
	outputs = {self, nixpkgs, flake-utils, ... }: 
		let
			system = "x86_64-linux";
			pkgs = import nixpkgs {
				inherit system;
			};
		in rec {
			packages.${system} = {
				default = pkgs.poetry2nix.mkPoetryApplication { projectDir = self; };
			};
			apps = rec {
				sysFetch = {
					type = "app";
					program = "${self.packages.${system}.default}/bin/sysfetch";
				};
				default = sysFetch;
			};
			devShells.default = pkgs.mkShell {
				buildInputs = with pkgs; [
					python3
					poetry
				];
			};
		};
}
