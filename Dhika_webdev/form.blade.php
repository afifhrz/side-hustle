@extends('master.master')
@section('custom_style')

@stop

@section('title')
    CODE | Form
@stop

@section('content')
    <div class="row">
        <div class="col-lg-6 grid-margin">
            <div class="card">
                <div class="card-body">
                    <h2><b>Form</b></h2><br />
                    <form action="{{ route('saveusersmodify') }}" method="POST">
                        @csrf
                        <div class="form-group">
                            <label>Name</label>
                            <input type="text" name="name" value="{{ old('name') }}" class="form-control"
                                style="width:40%;" />
                            <span style="color:red">{{ $errors->first('name') }}</span>
                        </div>
                        <div class="form-group">
                            <label>Email</label>
                            <input type="email" name="email" value="{{ old('email') }}" class="form-control"
                                style="width:40%;" />
                            <span style="color:red">{{ $errors->first('email') }}</span>
                        </div>
                        <div class="form-group">
                            <label>Password</label>
                            <input type="password" name="password" class="form-control" style="width:40%;" />
                            <span style="color:red">{{ $errors->first('password') }}</span>
                        </div>
                        <div class="form-group">
                            <label>Re-Password</label>
                            <input type="password" name="password_confirmation" class="form-control" style="width:40%;" />
                            <span style="color:red">{{ $errors->first('confirm_password') }}</span>
                        </div>
                        <div class="form-group">
                            <label>Date of Birth</label>
                            <input type="date" name="dob" value="{{ old('dob') }}"class="form-control"
                                style="width:30%;" /><br />
                            <span style="color:red">{{ $errors->first('dob') }}</span>
                        </div>
                        <div class="form-group">
                            <label>Gender</label>
                            <select class="form-control" name="gender" value="{{ old('gender') }}" style="width:30%;">
                                <option value="">Select Gender</option>
                                <option @if (old('gender') == 'M') selected @endif value="M">Male</option>
                                <option @if (old('gender') == 'F') selected @endif value="F">Female</option>
                            </select>
                            <span style="color:red">{{ $errors->first('gender') }}</span>
                        </div>
                        <button type="submit" class="btn btn-primary">Save</button>
                    </form>
                </div>
            </div>
        </div>
        <div class="col-lg-6 grid-margin">
            <div class="card">
                <div class="card-body">
                    <h2><b>Form</b></h2><br />
                    <form action="{{ route('saveusersmodify') }}" method="POST">
                        @csrf
                        <div class="form-group">
                            <label>Name</label>
                            <input type="text" name="name" value="{{ old('name') }}" class="form-control"
                                style="width:40%;" />
                            <span style="color:red">{{ $errors->first('name') }}</span>
                        </div>
                        <div class="form-group">
                            <label>Email</label>
                            <input type="email" name="email" value="{{ old('email') }}" class="form-control"
                                style="width:40%;" />
                            <span style="color:red">{{ $errors->first('email') }}</span>
                        </div>
                        <div class="form-group">
                            <label>Password</label>
                            <input type="password" name="password" class="form-control" style="width:40%;" />
                            <span style="color:red">{{ $errors->first('password') }}</span>
                        </div>
                        <div class="form-group">
                            <label>Re-Password</label>
                            <input type="password" name="password_confirmation" class="form-control" style="width:40%;" />
                            <span style="color:red">{{ $errors->first('confirm_password') }}</span>
                        </div>
                        <div class="form-group">
                            <label>Date of Birth</label>
                            <input type="date" name="dob" value="{{ old('dob') }}"class="form-control"
                                style="width:30%;" /><br />
                            <span style="color:red">{{ $errors->first('dob') }}</span>
                        </div>
                        <div class="form-group">
                            <label>Gender</label>
                            <select class="form-control" name="gender" value="{{ old('gender') }}" style="width:30%;">
                                <option value="">Select Gender</option>
                                <option @if (old('gender') == 'M') selected @endif value="M">Male</option>
                                <option @if (old('gender') == 'F') selected @endif value="F">Female</option>
                            </select>
                            <span style="color:red">{{ $errors->first('gender') }}</span>
                        </div>
                        <button type="submit" class="btn btn-primary">Save</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
@stop
@section('custom_script')

@stop
